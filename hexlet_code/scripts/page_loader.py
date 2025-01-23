#!/usr/bin/env python
from hexlet_code.cmd_parser import parse_args
from hexlet_code.page_loader import download


def main():
    args = parse_args()
    print(download(args.url_to_download, args.output))


if __name__ == "__main__":
    main()
