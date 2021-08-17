#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from src.producer import Producer
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

class Display(tk.Frame):

    """
    - Responsible for UI
    - Methods:
        - __init__()
    """

    def __init__(self, master:tk.Tk=None) -> None:
        super().__init__(master)
        self.__master = master
        self.__prd = Producer()
        self.__master.wm_title("Queue Simulator")
        self.__master.geometry("900x600")
        self.__fig = Figure(figsize=(6, 4), dpi=100)
        self.__canvas = FigureCanvasTkAgg(self.__fig, master=self)
        self.__x = []
        self.__y = []
        self.__subplot = None
        self.__line = None
        self.__widgets()
        self.pack()

    def __widgets(self) -> None:
        """
        - Starts all UI widgets
        - Params:
            - None
        - Returns:
            - None
        """
        self.__subplot = self.__fig.add_subplot(111)
        self.__subplot.set_xlabel("Sequence size")
        self.__subplot.set_ylabel("Sequence numbers")
        self.__line, = self.__subplot.plot(self.__x, self.__y, 'ro')
        self.__canvas.draw()

        self.__canvas.get_tk_widget().grid(row=0, columnspan=2)

        tk.Label(self, text="x").grid(row=1, column=0)
        tk.Label(self, text="a").grid(row=2, column=0)
        tk.Label(self, text="c").grid(row=3, column=0)
        tk.Label(self, text="m").grid(row=4, column=0)
        tk.Label(self, text="n").grid(row=5, column=0)

        x = tk.Entry(self, textvariable=tk.IntVar())
        x.grid(row=1, column=1)
        a = tk.Entry(self, textvariable=tk.IntVar())
        a.grid(row=2, column=1)
        c = tk.Entry(self, textvariable=tk.IntVar())
        c.grid(row=3, column=1)
        m = tk.Entry(self, textvariable=tk.IntVar())
        m.grid(row=4, column=1)
        n = tk.Entry(self, textvariable=tk.IntVar())
        n.grid(row=5, column=1)

        entries = [x, a, c, m, n]

        tk.Button(self, text="Submit", command=(lambda e = entries: self.__plot(e))).grid(row=6, column=0)
        tk.Button(self, text="Quit", command=self.__master.destroy).grid(row=6, column=1)

        self.update()

    def __plot(self, e) -> None:
        """
        - Plot chart for random sequence at UI
        - Params:
            - None
        - Returns:
            - None
        """
        x = int(e[0].get())
        a = int(e[1].get())
        c = int(e[2].get())
        m = int(e[3].get())
        n = int(e[4].get())
        sequence = self.__prd.generate(x, a, c, m, n)
        x = list(range(0, len(sequence)))
        y = sequence
        self.__line.set_data(x, y)
        ax = self.__canvas.figure.axes[0]
        ax.set_xlim(min(x)-1, max(x)+1)
        ax.set_ylim(min(y)-1, max(y)+1)
        self.__canvas.draw()
