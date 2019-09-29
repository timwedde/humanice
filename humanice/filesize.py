#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bits & Bytes related humanization."""

suffixes = {
    'decimal': ('kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
    'binary': ('KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'),
    'gnu': "KMGTPEZY",
}


def naturalsize(value, binary=False, gnu=False, format='{:.1f}'):
    """Format a number of bytes like a human readable filesize (eg. 10 kB).  By
    default, decimal suffixes (kB, MB) are used.  Passing binary=true will use
    binary suffixes (KiB, MiB) are used and the base will be 2**10 instead of
    10**3.  If ``gnu`` is True, the binary argument is ignored and GNU-style
    (ls -sh style) prefixes are used (K, M) with the 2**10 definition.
    Non-gnu modes are compatible with jinja2's ``filesizeformat`` filter."""
    if gnu:
        suffix = suffixes['gnu']
    elif binary:
        suffix = suffixes['binary']
    else:
        suffix = suffixes['decimal']

    value = str(value)
    format_string = format
    base = 1024 if (gnu or binary) else 1000
    if value.startswith("-"):
        format_string = "-" + format_string
        value = value.replace("-", "")
    bytes = float(value)

    if bytes == 1 and not gnu:
        return '1 Byte'
    elif bytes < base and not gnu:
        return '{} Bytes'.format(int(bytes))
    elif bytes < base and gnu:
        return '{}B'.format(int(bytes))

    for i, s in enumerate(suffix):
        unit = base ** (i + 2)
        if bytes < unit - base and not gnu:
            return (format_string + " {}").format(base * bytes / unit, s)
        elif bytes < unit - base and gnu:
            return (format_string + "{}").format(base * bytes / unit, s)
    if gnu:
        return (format_string + "{}").format(base * bytes / unit, s)
    return (format_string + " {}").format(base * bytes / unit, s)
