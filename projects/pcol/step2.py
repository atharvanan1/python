#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(prog='pcol')
parser.add_argument('--foo', nargs='?', help='foo of the %(prog)s program')
parser.add_argument('bar', nargs='+', help='bar of the %(prog)s program')
args = parser.parse_args()
print(args)
