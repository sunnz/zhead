zhead
=====
zhead is a gzip decompressing version of the nix command head
as in zcat is a gzip decompressing version of nix command cat.

that's right, there are no zhead command. yes you can to a zcat FILE | head
and it will do, you can also do a gzip -cd FILE and its essentially zcat.
see cat /bin/zcat, or cat /usr/bin/zless.

zhead is implemented in python 3.x for the fun of it, that's ALL.
