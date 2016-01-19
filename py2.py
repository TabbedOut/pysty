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
        reformatted_code, changed = FormatCode('\n'.join(self.lines[1:-1]))
        # Always insert a blank line before the counterexample
        return '\n```lang=python\n{}```'.format(reformatted_code)


def chunkify(lines):
    """
    Split lines of text into text, counterexamples, and examples.
    """
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


def insert_corrected(chunks):
    """
    Make sure counterexamples are followed by an example.

    Returns an iterable of str.
    """
    chunks = list(chunks)
    n_chunks = len(chunks)
    for idx, chunk in enumerate(chunks):
        yield str(chunk)
        if (chunk.kind == COUNTEREXAMPLE and
                (idx > (n_chunks - 3) or chunks[idx + 2].kind != CODE)):
            yield chunk.corrected


def process(original_text):
    chunks = chunkify(original_text.splitlines())
    return '\n'.join(insert_corrected(chunks))


def main(path):
    with open(path) as fh:
        original_text = fh.read()

    new_text = process(original_text)
    print(new_text)


if __name__ == '__main__':
    process(sys.argv[1])
