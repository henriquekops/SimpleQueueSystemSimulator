#!/usr/bin/env python
# -*- coding: utf-8 -*-

from art import tprint
import tkinter as tk
from src import (
    display
)

if __name__ == '__main__':
    tprint("Queue simulator", font="cybermedium")
    root = tk.Tk()
    d = display.Display(master=root)
    d.mainloop()
