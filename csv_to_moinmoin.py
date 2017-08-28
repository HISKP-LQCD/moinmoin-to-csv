#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT/Expat license.

import argparse
import csv

def main():
    options = _parse_args()

    with open(options.input) as f:
        reader = csv.reader(f)
        rows = list(reader)

    print(rows)

    if options.header:
        rows[0] = ["'''{}'''".format(cell) for cell in rows[0]]

    if options.link:
        offset = 1 if options.header else 0
        rows[offset:] = [
            ['[[{}]]'.format(row[0])] + row[1:]
            for row in rows[offset:]
        ]

    widths = [
        max(map(len, col))
        for col in zip(*rows)
    ]

    formats = ['{{:{}s}}'.format(width) for width in widths]
    format = '|| ' + ' || '.join(formats) + ' ||\n'

    with open(options.output, 'w') as f:
        for row in rows:
            f.write(format.format(*row))


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--header', action='store_true')
    parser.add_argument('--link', action='store_true')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
