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
        if kind in (CODE, COUNTEREXAMPLE):
            try:
                assert lines[0].startswith('```')
                assert lines[-1] == '```'
            except AssertionError:
                raise TypeError('Input lines do not look like code')

    def __repr__(self):
        return '\n'.join(self.lines)

    @property
    def corrected(self):
        if self.kind != COUNTEREXAMPLE:
            raise TypeError('Can only correct COUNTEREXAMPLE chunks')
        # Always insert a blank line before the counterexample
        return '\n```lang=python\n{}```'.format(
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
    new_text_chunks = []
    for chunk in chunkify(original_text.splitlines()):
        if chunk.kind != CODE:
            new_text_chunks.append(str(chunk))
        if chunk.kind == COUNTEREXAMPLE:
            new_text_chunks.append(chunk.corrected)
    return '\n'.join(new_text_chunks)


def main(path):
    with open(path) as fh:
        original_text = fh.read()

    new_text = process(original_text)
    print(new_text)


if __name__ == '__main__':
    process(sys.argv[1])
