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

# See: http://effbot.org/tkinterbook/menu.htm

# "Toplevel menus are displayed just under the title bar of the root or any
# other toplevel windows (or on Macintosh, along the upper edge of the screen).
# To create a toplevel menu, create a new Menu instance, and use add methods to
# add commands and other menu entries to it."

import tkinter as tk

def hello():
    print("Hello!")

def main():
    """Main function"""

    root = tk.Tk()

    # Create a toplevel menu
    menubar = tk.Menu(root)
    menubar.add_command(label="Hello", command=hello)
    menubar.add_command(label="Quit", command=root.quit)

    # Display the menu
    root.config(menu=menubar)

    root.mainloop()

if __name__ == '__main__':
    main()