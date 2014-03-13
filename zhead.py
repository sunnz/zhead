#!/usr/bin/env python3

import argparse, gzip

def main():
    parser = argparse.ArgumentParser(description='Uncompress filename and print the  first 10 lines to standard output.')
    parser.add_argument('filename', help='filename of the compressed text file.')
    args = parser.parse_args()

    with gzip.open(args.filename, 'rt') as f:
        print(f.readline(), end='')

if __name__ == '__main__':
    main()
