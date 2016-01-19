from __future__ import unicode_literals

import pytest

import py2


TEXT = """
# Are you suggesting that coconuts migrate?

What do you mean? Shut up! A newt? You don't vote for kings. You can't expect to wield supreme power just 'cause some watery tart threw a sword at you!

## Bloody Peasant!

What a strange person. Well, I got better. Look, my liege! Well, how'd you become king, then? Well, how'd you become king, then?

1. Found them? In Mercia?! The coconut's tropical!
2. I dunno. Must be a king.
3. Camelot!

```lang=python, counterexample
import antigravity
```

Why? I don't want to talk to you no more, you empty-headed animal food trough water! I fart in your general direction! Your mother was a hamster and your father smelt of elderberries! Now leave before I am forced to taunt you a second time!
""".strip()

TARGET_TEXT = """

```lang=python, counterexample
import antigravity
```

```lang=python
import antigravity
```

"""

MIXED_CODE_TEXT = """

Knights of Ni, we are but simple travelers who seek the enchanter who lives
beyond these woods.

```lang=python, counterexample
import antigravity
```

```lang=python
import antigravity
```


"""


def test_chunk_code_must_look_like_code():
    with pytest.raises(TypeError):
        py2.Chunk(['', 'chunk', ''], kind=py2.CODE)

    with pytest.raises(TypeError):
        py2.Chunk(['```', 'chunk', ''], kind=py2.CODE)

    with pytest.raises(TypeError):
        py2.Chunk(['', 'chunk', '```'], kind=py2.CODE)


def test_chunk_repr_preserves_whitespace():
    chunk = py2.Chunk(['', 'chunk', ''])
    assert str(chunk) == chunk.__repr__()
    assert str(chunk) == '\nchunk\n'


def test_chunk_corrected_only_works_on_code():
    chunk = py2.Chunk(['', 'chunk', ''])
    with pytest.raises(TypeError):
        chunk.corrected


def test_chunkify_splits_text_into_chunks():
    chunks = py2.chunkify(TEXT.splitlines())
    assert len(list(chunks)) == 3


def test_chunkify_splits_whitespaced_text_into_chunks():
    chunks = list(py2.chunkify(MIXED_CODE_TEXT.splitlines()))
    assert len(chunks) == 5
    assert str(chunks[0]).startswith('\n\n')
    assert str(chunks[0]).endswith('\n')
    assert chunks[1].kind == py2.COUNTEREXAMPLE
    assert str(chunks[2]) == ''
    assert chunks[3].kind == py2.CODE
    assert str(chunks[4]) == '\n'


def test_chunkify_preserves_whitespace():
    chunks = list(py2.chunkify(TEXT.splitlines()))

    assert chunks[0].kind == py2.TEXT
    assert chunks[0].lines[-1] == ''

    assert chunks[1].kind == py2.COUNTEREXAMPLE
    assert chunks[1].lines[0] == '```lang=python, counterexample'
    assert chunks[1].lines[-1] == '```'

    assert chunks[2].kind == py2.TEXT
    assert chunks[2].lines[0] == ''


def test_process_leaves_regular_text_alone():
    original_text = 'The Knights Who Say Ni demand a sacrifice!'
    assert py2.process(original_text) == original_text


def test_process_inserts_correction():
    assert TARGET_TEXT in py2.process(TEXT)


# def test_process_a_process_is_idempotent():
#     first_pass = py2.process(TEXT)
#     assert py2.process(py2.process(first_pass)) == first_pass
