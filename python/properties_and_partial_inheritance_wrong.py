#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
This snippet test Python properties.

See: https://docs.python.org/3/library/functions.html#property
"""

class Foo(object):

    def __init__(self):
        self._x = None

    def get_x(self):
        print('call get_x from Foo')
        return self._x

    def set_x(self, value):
        print('call set_x from Foo: ', value)
        self._x = value

    def del_x(self):
        print('call del_x from Foo')
        del self._x

    x = property(get_x, set_x, del_x, "The 'x' property docstring (Foo).")


class Bar(Foo):

    def set_x(self, value):                   # If only set_x is defined, it doesn't work...
        print('call set_x from Bar: ', value)
        self._x = value


def main():
    """Main function"""

    foo = Foo() 

    print(foo.x)
    print()

    foo.x = 3

    print(foo.x)
    print()

    print(Foo.x.__doc__)

if __name__ == '__main__':
    main()
