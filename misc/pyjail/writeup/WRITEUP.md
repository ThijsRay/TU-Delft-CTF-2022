# Pyjail

## Description
This challenge required you to read a flag.txt file on the server with a restricted python REPL.

## Solution
The challenge can be solved by understanding that python also loads `site_modules` by defaults so these are included in the global variables.
One of the instances included in this is the `license` variable. Which is an instance of the `_Printer` class. I included an annotated source code of the `_Printer` class below.

```python
class _Printer(object):
    """interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice."""

    MAXLINES = 23

    def __init__(self, name, data, files=(), dirs=()):
        import os # 👀 os gets imported here
        self.__name = name
        self.__data = data
        self.__lines = None
        self.__filenames = [os.path.join(dir, filename)
                            for dir in dirs
                            for filename in files]

    def __setup(self):
        if self.__lines:
            return # so if lines is None we can continue
        data = None
        for filename in self.__filenames:
            try:
                with open(filename, encoding='utf-8') as fp:
                    data = fp.read() # 🙀 We will iterate over all the files in the __filenames list and read the data
                break
            except OSError:
                pass
        if not data:
            data = self.__data
        self.__lines = data.split('\n')
        self.__linecnt = len(self.__lines)

    ### 🤔 Hmm, this is all fun and games. But since we cannot call functions, how do we get the flag?

    ### Wait whats this 👀
    # A __repr__ method is called when you try to print an object, which is coincidentally what the challenge is doing when showing changed variables in the REPL
    def __repr__(self):
        # And there it is... The fabled __setup method call
        self.__setup()
        if len(self.__lines) <= self.MAXLINES:
            return "\n".join(self.__lines)
        else:
            return "Type %s() to see the full %s text" % ((self.__name,)*2)

    def __call__(self):
        self.__setup()
        prompt = 'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
        while 1:
            try:
                for i in range(lineno, lineno + self.MAXLINES):
                    print(self.__lines[i])
            except IndexError:
                break
            else:
                lineno += self.MAXLINES
                key = None
                while key is None:
                    key = input(prompt)
                    if key not in ('', 'q'):
                        key = None
                if key == 'q':
                    break
```

So in short, `print(license)` calls `__setup` which reads all files inside `license.__filenames`, if `license.__lines` is `None`. Great... we're done right?

_Not so fast..._

Another problem is that we cannot create strings. There is a way to create individual chars but since string concatenation is impossible* we cannot create a string that contains the flag. However there is another trick.

## What can the `open()` method do anyway?
Looking at the documentation we can see a small section about the `open()` method. It says that you can pass a file descriptor to the `open()` method. This is a way to open a file without using a path. This is useful when you want to open a file that is not on the filesystem but in memory. This is exactly what we need.

See there are some special file descriptors that you can use. One of them is `0` which is the standard input. So if we manage to run `open(0)` you can just type whatever string you want and it will be read.

# The final solution

The final solution will be in the form of a number of python lines to be run in the REPL.
    
```python
# Set up everything in order to run the open(0) method
license._Printer__filenames=[0]
license._Printer__lines=None
out = license
# After running this you get an empty prompt. Here you can type "flag.txt" and then close the stdin with ctrl+d or ctrl+z
# now your input is stored in the license
data = license._Printer__lines[0]
# data now contains: "flag.txt"
license._Printer__filenames=[data]
license._Printer__lines=None
# setup everything to run the open("flag.txt") method
out2 = license
# And there you go. 
# print(license) --> license.__repr__() -> license.__setup() --> open("flag.txt")
```
---
\* It might be technically possible to create a string without the open(0) method using decorators. Provided you have all the characters in the alphabet. It would look something like this, courtesy of luke.

```python
x = license
y = []

@x.__filepath.insert
@"".join
@lambda x: ["f", "l", "a", "g", ".", "t", "x", "t"]
class X: pass
```