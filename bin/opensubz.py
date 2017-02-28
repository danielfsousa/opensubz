#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

import opensubz.context_menu as context_menu
from opensubz.config import Config
from opensubz.core import OpenSubz


def main():
    try:

        parser = get_parser()
        args = parser.parse_args()
        config = Config()

        check_config(config)

        if args.search:
            lang = args.language if args.language else config.language
            if lang.strip():
                OpenSubz.search(args.search, lang)
            else:
                OpenSubz.search(args.search)

        elif args.config:
            set_account(config)

        elif args.install:
            context_menu.install()

        elif args.uninstall:
            context_menu.uninstall()

        else:
            parser.print_help()

    except KeyboardInterrupt:
        pass


def check_config(config):
    if (not config.email) or (not config.password):
        print("""
        We need to set your opensubtitles account first.
        If you don't have one you can register here: https://www.opensubtitles.org/newuser
        """)
        set_account(config)


def set_account(config):
    config.email = input('Email: ')
    config.password = input('Password: ')
    print('\n*** Check all available language codes: http://www.loc.gov/standards/iso639-2/php/code_list.php')
    print('*** Default: eng\n')
    config.language = input('Prefered language (ISO 639-2 code): ')
    config.save()


def get_parser():

    class MyParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser(description="""
    opensubz 0.1.0

    Author: Daniel Sousa
    Email: sousa.dfs@gmail.com
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--search', action='store', required=False, help='Path containing .mkv or .mp4 files to search for subtitles')
    parser.add_argument('-l', '--language', action='store', help='Filter subtitles by the language code provided.'
    '\nCheck all available language codes: http://www.loc.gov/standards/iso639-2/php/code_list.php')
    parser.add_argument('-i', '--install', action='store_true', default=False, help='Add download option in the Windows context menu')
    parser.add_argument('-u', '--uninstall', action='store_true', default=False, help='Remove download option in the Windows context menu')
    parser.add_argument('-c', '--config', action='store_true', default=False, help='Set your opensubtitles account and preferences')
    return parser

