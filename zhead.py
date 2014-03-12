#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='Uncompress filename and print the  first 10 lines to standard output.')
    parser.add_argument('filename', help='filename of the compressed text file.')
    args = parser.parse_args()
    print(args.filename)

if __name__ == '__main__':
    main()
