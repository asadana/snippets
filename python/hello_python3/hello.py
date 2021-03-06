#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Jérémie DECOCK (http://www.jdhp.org)

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
This module does blah blah.

Here is the description of the module.
See PEP 257 (http://legacy.python.org/dev/peps/pep-0257/) for more details.
See also http://stackoverflow.com/questions/2557110/what-to-put-in-a-python-module-docstring.

See also PEP 8 (http://legacy.python.org/dev/peps/pep-0008/) for Python's good practices.
"""

import sys, os

def main():
    """
    This function does blah blah.
    
    Here is the description of the function.
    See PEP 257 (http://legacy.python.org/dev/peps/pep-0257/) for more details.

    See also PEP 8 (http://legacy.python.org/dev/peps/pep-0008/) for Python's good practices.
    """

    # Print the python version
    # The follow syntax only works with Python 3.x: a, b, *rest = sequence
    # This script can't be executed with Python 2.x (not even with Python 2.7)
    version, *rest = sys.version.split(' ')
    print("Hello from Python", version, os.linesep)

    print("Hello!")
    print("¡Buenos días!")
    print("Bonjour!")
    print("你好！")

if __name__ == '__main__':
    main()
