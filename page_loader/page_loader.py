__all__ = ['download']
import requests
import os
import re
from urllib.parse import urlsplit, urlunsplit
from bs4 import BeautifulSoup
from page_loader.app_logger import get_logger

logger = get_logger(__name__)


def download(url, path):
    parsed_page_url = urlsplit(url)
    name_from_url = make_name(parsed_page_url)
    logger.info(f"requested url: {url}")
    logger.info(f"output path: {os.path.abspath(path)}")
    html_file_path = get_html(url, path, name_from_url)
    logger.info(f"write html file: {html_file_path}")
    dir_abs_path = make_dir(name_from_url, path)
    try:
        with open(html_file_path, "r") as fr:
            soup = BeautifulSoup(fr, "html.parser")
            if soup.find_all("img", src=True):
                dwl_cont_mod_html(
                    soup, parsed_page_url, dir_abs_path, "img", "src"
                )
            if soup.find_all("link", href=True):
                dwl_cont_mod_html(
                    soup, parsed_page_url, dir_abs_path, "link", "href"
                )
            if soup.find_all("script", src=True):
                dwl_cont_mod_html(
                    soup, parsed_page_url, dir_abs_path, "script", "src"
                )
            with open(html_file_path, "w") as fw:
                print(soup.prettify().strip(), file=fw)
    except PermissionError as e:
        logger.debug(f'Received an error {e} when creating a file')
        logger.error(
            f"Can't create '{html_file_path}' – no permission to directory"
        )
        raise Exception() from e
    except:
        logger.error(f'Received an  unexpected error when creating a file')
        raise Exception()
    return html_file_path


def make_name(parsed_url):
    path = parsed_url.path
    pattern = r"(.+?)(?:\.\w*)?$"
    path_without_exe = re.search(pattern, path)[1]
    raw_name = parsed_url.netloc + path_without_exe
    new_name = re.sub(r"\W", "-", raw_name)
    logger.debug(f"Get name '{new_name}' from path: '{path}'")
    return new_name


def get_html(url, path, name):
    file_name = name + ".html"
    new_file_path = os.path.join(path, file_name)
    try:
        with requests.get(url, timeout=10) as response:
            response.raise_for_status()
            html = response.text
        with open(new_file_path, "w") as f:
            print(html, file=f, end="")
    except requests.exceptions.HTTPError as e:
        logger.debug(f'Request to url get error {e}')
        logger.error(f"Bad status code – {e}")
        raise Exception() from e
    except PermissionError as e:
        logger.debug(f'Received an error {e} when creating a file')
        logger.error(
            f"Can't create '{new_file_path}' – no permission to directory"
        )
        raise Exception() from e
    except:
        logger.error(f'Received an  unexpected error when creating a file')
        raise Exception()
    return os.path.abspath(new_file_path)


def make_dir(name, path):
    dir_name = name + "_files"
    new_dir_path = os.path.join(path, dir_name)
    try:
        os.mkdir(new_dir_path)
    except OSError as e:
        logger.debug(f'Received an error {e} when creating the directory')
        logger.error(
            f"Directory '{dir_name}' already exist"
            f" or no permission to create it"
        )
        raise Exception() from e
    except:
        logger.error(f'Received an  unexpected error when creating the directory')
        raise Exception()
    return os.path.abspath(new_dir_path)


def dwl_cont_mod_html(soup, parsed_page_url, dir_abs_path, _tag, _attr):
    files_dir_name = os.path.basename(dir_abs_path)
    for tag in soup.find_all(_tag, attrs={_attr: True}):
        cont_url = urlsplit(tag[_attr])
        if cont_url.netloc and cont_url.netloc != parsed_page_url.netloc:
            pass
        else:
            cont_url = parsed_page_url._replace(
                path=cont_url.path,
                query=cont_url.query,
                fragment=cont_url.fragment,
            )
            new_cont_name = make_name(cont_url)
            if len(cont_url.path.split(".")) > 1:
                new_cont_name = (
                    new_cont_name + "." + cont_url.path.split(".")[-1]
                )
            if len(cont_url.path.split(".")) == 1 and _attr == "href":
                html_path = get_html(
                    urlunsplit(cont_url), dir_abs_path, new_cont_name
                )
                tag[_attr] = os.path.join(
                    files_dir_name, os.path.basename(html_path)
                )
                continue
            cont_abs_path = os.path.join(dir_abs_path, new_cont_name)
            get_cont(urlunsplit(cont_url), cont_abs_path)
            tag[_attr] = os.path.join(files_dir_name, new_cont_name)
    return soup


def get_cont(cont_url, path):
    try:
        with requests.get(cont_url, stream=True, timeout=10) as response:
            response.raise_for_status()
            chunked_content = response.iter_content(8192)
            with open(path, "bw") as f:
                for chunk in chunked_content:
                    f.write(chunk)
    except requests.exceptions.HTTPError as e:
        logger.debug(f'Request to url received an error {e}')
        logger.error(f"Bad status code – {e}")
        raise Exception() from e
    except PermissionError as e:
        logger.debug(f'Received an error {e} when creating a file')
        logger.error(f"Can't create '{path}' – no permission to directory")
        raise Exception() from e
    except:
        logger.error(f'Received an  unexpected error when creating a file')
        raise Exception()
