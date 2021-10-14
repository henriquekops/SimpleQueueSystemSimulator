#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from art import tprint
import tkinter as tk
from src.simulator import Simulator
from src import (
    display
)

help =         """ You can fowlling the model:\n 
            python3 main.py [n] [use_loss] [start] [capacities] [servers] [minArrivals] [maxArrivals] [minExits] [maxExits]
            
            Glossary:

            n           ->
            use_loss    ->
            start       ->
            capacities  ->
            servers     ->
            minArrivals ->
            maxArrivals ->
            minExits    ->
            maxExits    ->
            
            
            """

"""
TODO: 
    - Ler arquivo de entrada (cuidar criação do Producer() na classe Simulator())
    - Permitir a leitura de uma sequência de 'aleatórios' previamente calculados
"""

if __name__ == '__main__':
    
    tprint("Queue simulator", font="cybermedium")
    
    args = argv

    if len(argv) == 1:
        print(help)

    elif args[1] == 'teacher':
        root = tk.Tk()
        d = display.Display(master=root)
        d.mainloop()

    else:
        try:
            # args = [int(i) for i in args if i.isnumeric()]
            Simulator(n=int(args[1]), use_loss=bool([2])).init(
                start=int(args[3]),
                capacities=[int(x) for x in list(args[4])],
                servers=[int(x) for x in list(args[5])],
                minArrivals=[int(x) for x in list(args[6])],
                maxArrivals=[int(x) for x in list(args[7])],
                minExits=[int(x) for x in list(args[8])],
                maxExits=[int(x) for x in list(args[9])]
            )
        except Exception as e:
            print(e)
            print(help)
