zhead
=====
zhead is a gzip decompressing version of the nix command head
as in zcat is a gzip decompressing version of nix command cat.

that's right, there are no zhead command. yes you can do a zcat FILE | head
and it will do, you can also do a gzip -cd FILE and its essentially zcat.
see cat /bin/zcat, or cat /usr/bin/zless.

zhead is implemented in python 3.x for the fun of it, that's ALL.

## current state

it can take a gzipped file and print the first N
lines of it, passed with -n option, default to 10.

it doesn't take anything other than ONE filename,
no option to take more than 1 file,
throws an horrible uncaught exception/error when the format is in fact
plain text or simply not gzip, and not tested with a binary file
that happens to be gzipped.

## license

zhead is available under the ISC license:

> Copyright (c) 2014, sunnz (https://github.com/sunnz)
> 
> Permission to use, copy, modify, and/or distribute this software for any
> purpose with or without fee is hereby granted, provided that the above
> copyright notice and this permission notice appear in all copies.
> 
> THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
> WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
> MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
> ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
> WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
> ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
> OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
