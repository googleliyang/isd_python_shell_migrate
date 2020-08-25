#! /usr/bin/env python3

import argparse
import os
from distutils.dir_util import copy_tree

from src.run import Helper

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='爱山东代码改造脚本.')
    parser.add_argument('--file', metavar='操作文件夹路径', type=str, help='source file')
    args = parser.parse_args()
    files = args.file
    if not os.path.isdir(files):
        print('error file format')
        exit()
    helper = Helper(files)
    helper.ready_file()
    # helper.rm_token_of_headers()
    pass
