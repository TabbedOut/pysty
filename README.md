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
includes HTML/JavaScript.) The only exemption I can think of is URLs.

```lang=python, counterexample
class MyClass(object):
    def __init__(self):
        """
        Example init that goes on way too long to illustrate what a bad docstring looks like.

        https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        """
        pass
```

```lang=python
class MyClass(object):

    def __init__(self):
        """
        Example init that goes on way too long to illustrate what a bad docstring looks like.

        https://phab.tabbedout.com/w/development/style_guide/python/#indention-and-long-lines
        """
        pass
```

### Snake case

```lang=python, counterexample
def doTheThing():
    pass
```

```lang=python
def doTheThing():
    pass
```

### Blank lines

```lang=python, counterexample
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
````
