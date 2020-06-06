#!/bin/sh
if ! test -n "$1"
then
	echo Usage "$0" file.tsv >&2
	exit 1
fi
make maplot
python3 maplot/plot.py "$1"
