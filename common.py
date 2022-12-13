import sys as _sys
import dataclasses as _dataclasses

#
# Reexports
#

from string import (
    ascii_letters as LETTERS,
    ascii_lowercase as LOWERCASE,
    ascii_uppercase as UPPERCASE,
    digits as DIGITS,
)
import itertools
import re

#
# Utility
#


def qdataclass(fields, name="Q"):
    """create a dataclass as if every space-delimited name in `fields` was an Any type field"""

    return _dataclasses.make_dataclass(name, fields.split())


def convert(input_list, output_list, some_val_from_input_list):
    try:
        return output_list[input_list.index(some_val_from_input_list)]
    except ValueError:
        return None


def _fixedgroups(alist, size):
    cur = 0
    lmax = len(alist)

    if lmax % size != 0:
        print("The number of items is not a multiple of size")

    while cur < lmax:
        yield alist[cur : cur + size]
        cur += size


def listchunks(alist, size):
    """return sublists from `alist` each `size` long"""
    return list(_fixedgroups(alist, size))


def indexbykey(alist, key):
    for i, item in enumerate(alist):
        if key(item):
            return i


def _sepgroup(lines, sep, start=None):
    start = start or 0
    cur = start
    while cur < len(lines):
        if lines[cur] == sep:
            return (lines[start:cur], cur + 1)
        cur += 1
    return (lines[start:], len(lines))


def _sepgroups(alist, sep):
    cur = 0
    while cur < len(alist):
        group, endspot = _sepgroup(alist, sep=sep, start=cur)
        yield group
        cur = endspot


def listsplit(alist, sep):
    return list(_sepgroups(alist, sep))


def iternone(iterable):
    """iter that yields None instead of raising StopIteration"""
    itr = iter(iterable)
    while True:
        try:
            yield next(itr)
        except StopIteration:
            yield None


def _striptrailingnewlines(s):
    for i in range(1, len(s)):
        if s[-i] not in "\n\r":
            return s[: -i + 1]
    return ""


#
# Input from files
# All of the inf* functions return the contents of the file that is given by path on the
# command line.
#


def inf(path=None):
    """input file"""

    if path is None:
        path = _sys.argv[1]

    return open(path)


def inf_lraw(path=None):
    """input lines"""
    return inf(path=path).readlines()


def inf_lstripnewlines(path=None):
    """input lines, trailing newlines stripped"""
    return [_striptrailingnewlines(l) for l in inf_lraw(path=path)]


def inf_lstrip(path=None):
    """input lines, stripped"""
    return [l.strip() for l in inf_lraw(path=path)]
