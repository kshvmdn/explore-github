#!/usr/bin/env python

import argparse

from parser import main as get_data
from write import write_data

parser = argparse.ArgumentParser(description='View repositories for any GitHub account.')
parser.add_argument('user', type=str, help='GitHub user handle')
parser.add_argument('-f', '--format', choices=['json', 'csv', 'md', 'txt'],
                    help='File output format.')

args = parser.parse_args()
user, format_ = args.user, args.format

write_data(get_data(user), user, format_)

if __name__ == '__main__':
    user = 'kshvmdn'
    data = get_data(user)
    write_data(data, user, 'json')