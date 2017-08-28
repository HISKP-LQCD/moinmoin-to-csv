#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT/Expat license.

import argparse
import csv
import re


def moinmoin_table_to_native(lines):
    return list(map(moinmoin_line_to_native, lines))


def moinmoin_line_to_native(line):
    row = re.findall(r'\|\|\s*(.+?)\s*\|\|', line)
    row = list(map(deformat, row))
    return row


def deformat(cell):
    """
    Removes the formatting from a cell.

    This could be emphasis or a inter-wiki link. Markup that is removed:

    - Inter-wiki link, denoted by ``[[`` and ``]]``
    - Bold, denoted by ``'''`` and ``'''``
    """
    for pattern in ["'''", '[[', ']]']:
        cell = cell.replace(pattern, '')

    cell = re.sub(r',,(.+?),,', r'.\1', cell)

    return cell


def main():
    options = _parse_args()

    with open(options.input) as f:
        lines = list(f)

    native = moinmoin_table_to_native(lines)
    print(native)

    with open(options.output, 'w') as f:
        writer = csv.writer(f)
        for row in native:
            writer.writerow(row)


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input')
    parser.add_argument('output')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
