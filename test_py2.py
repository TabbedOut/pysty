from __future__ import unicode_literals

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
Why? Be quiet! Oh! Come and see the violence inherent in the system! Help, help, I'm being repressed!
```

Why? I don't want to talk to you no more, you empty-headed animal food trough water! I fart in your general direction! Your mother was a hamster and your father smelt of elderberries! Now leave before I am forced to taunt you a second time!
""".strip()


def test_chunkify_splits_text_into_chunks():
    chunks = py2.chunkify(TEXT.splitlines())
    assert len(list(chunks)) == 3


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
