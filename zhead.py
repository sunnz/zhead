#!/usr/bin/env python3

import argparse, gzip

def main():
    linecnt = 10

    parser = argparse.ArgumentParser(description='Uncompress filename and print the  first 10 lines to standard output.')
    parser.add_argument('-n', type=int, default=linecnt, metavar='COUNT', dest='linecnt')
    parser.add_argument('filename', help='filename of the compressed text file.')
    args = parser.parse_args()

    with gzip.open(args.filename, 'rt') as f:
        for cnt in range(args.linecnt):
            print(f.readline(), end='')

if __name__ == '__main__':
    main()
