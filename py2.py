#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Extract counterexamples from Markdown and add YAPF formatted examples.

Usage: py2.py <file>

Outputs to stdout
"""
from __future__ import unicode_literals

import sys

from yapf.yapflib.yapf_api import FormatCode


TEXT = 'text'
COUNTEREXAMPLE = 'counterexample'
CODE = 'code'


class Chunk(object):
    def __init__(self, lines, kind=TEXT):
        self.lines = lines
        self.kind = kind

    def __repr__(self):
        return '\n'.join(self.lines)

    @property
    def corrected(self):
        return '```lang=python\n{}```'.format(
            FormatCode('\n'.join(self.lines[1:-1]))[0])


def chunkify(lines):
    current_kind = TEXT
    current_chunk = []
    for line in lines:
        if line.startswith('```lang=python, counterexample'):
            yield Chunk(current_chunk)
            current_kind = COUNTEREXAMPLE
            current_chunk = [line]
        elif line.startswith('```lang=python'):
            yield Chunk(current_chunk)
            current_kind = CODE
            current_chunk = [line]
        elif current_kind != TEXT and line == '```':
            current_chunk.append(line)
            yield Chunk(current_chunk, kind=current_kind)
            current_chunk = []
            current_kind = TEXT
        else:
            current_chunk.append(line)
    yield Chunk(current_chunk)


def process(original_text):
    new_text = []
    for chunk in chunkify(original_text.splitlines()):
        # print '*' * 20, c.kind, '*' * 20  # DEBUG
        if chunk.kind != CODE:
            new_text.append(str(chunk))
        if chunk.kind == COUNTEREXAMPLE:
            new_text.append('')
            new_text.append(chunk.corrected)
    return ''.join(new_text)


def main(path):
    with open(path) as fh:
        original_text = fh.read()

    new_text = process(original_text)
    print(new_text)


if __name__ == '__main__':
    process(sys.argv[1])
