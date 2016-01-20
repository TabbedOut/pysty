Python Styleguide
=================

https://phab.tabbedout.com/w/development/style_guide/python/

Refer to PEP8 as the default style guide.

Whitespace
----------

Indent all code using 4 spaces.

```lang=python, counterexample
def foo():
  print('Hello World')
```

```lang=python
def foo():
    print('Hello World')
```

Keep lines to 79 characters or less. (This includes docstrings and sorta
includes HTML/JavaScript.) The only exception is URLs that are on their own
line, Restructured text, or Markdown.

```lang=python, counterexample
class MyClass(object):
    def __init__(self):
        """
        Example init that goes on way too long to illustrate what a bad docstring looks like.

        https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines

        [markdown]: https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        .. _rst: https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        """
        pass
```

```lang=python
class MyClass(object):

    def __init__(self):
        """
        Example init that goes on way too long to illustrate what a bad docstring looks like.

        https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines

        [markdown]: https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        .. _rst: https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        """
        pass
```

### Blank lines

```lang=python, counterexample
import os


from api import shim

class FooFactory(object):
    class Meta:
        name = 'foo'
    bar = None

class FooFighter(object):
    def one(self):
        pass
    def two(self):
        pass


    def three(self):
        pass
```

```lang=python
import os

from api import shim


class FooFactory(object):

    class Meta:
        name = 'foo'

    bar = None


class FooFighter(object):

    def one(self):
        pass

    def two(self):
        pass

    def three(self):
        pass
```
Have fun!

### Long imports

```lang=python, counterexample
from alphabet import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, q, r, s, t, u, v, w, x, y, z
from alphabet import (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, q, r, s, t, u, v, w, x, y, z)
from alphabet import (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, q, r, s, t, u, v, w, x, y, z,)
```

```lang=python
from alphabet import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, q, r, s, t, u, v, w, x, y, z
from alphabet import (
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, q, r, s, t, u, v, w, x, y, z)
from alphabet import (a,
                      b,
                      c,
                      d,
                      e,
                      f,
                      g,
                      h,
                      i,
                      j,
                      k,
                      l,
                      m,
                      n,
                      o,
                      q,
                      r,
                      s,
                      t,
                      u,
                      v,
                      w,
                      x,
                      y,
                      z, )
```

### Blank lines between imports

I'm not a fan of of how yapf removes a linebreak between the imports and code:

```lang=python, counterexample
import logging


logger = logging.getLogger(__name__)
class Foo(object):
  pass
```

```lang=python
import logging

logger = logging.getLogger(__name__)


class Foo(object):
    pass
```

### Braces and parens

```lang=python, counterexample
foo = {'the': 'rain', 'in': 'Spain', 'stays': 'mainly', 'on the': 'plains'}
bar({'pack': 'my', 'box': 'with', 'five': 'dozen', 'liquor': 'jugs'}, the=quick, brown=fox)
bar({'pack': 'my', 'box': 'with', 'five': 'dozen', 'liquor': 'jugs'},
    the=quick, brown=fox)
baz = {
  'now': 'what?',
}
```

```lang=python
foo = {'the': 'rain', 'in': 'Spain', 'stays': 'mainly', 'on the': 'plains'}
bar(
    {'pack': 'my',
     'box': 'with',
     'five': 'dozen',
     'liquor': 'jugs'},
    the=quick,
    brown=fox
)
bar(
    {'pack': 'my',
     'box': 'with',
     'five': 'dozen',
     'liquor': 'jugs'},
    the=quick,
    brown=fox
)
baz = {'now': 'what?', }
```
