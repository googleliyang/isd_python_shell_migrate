#! /usr/bin/env python3

import argparse
import os
from distutils.dir_util import copy_tree

from src.run import Helper

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Asd migrate Shell.')
    parser.add_argument('--file', metavar='output dir', type=str, help='source file')
    args = parser.parse_args()
    files = args.file
    if not os.path.isdir(files):
        print('error file format')
        exit()
    helper = Helper(files)
    helper.ready_file()
    # helper.rm_token_of_headers()
    pass
