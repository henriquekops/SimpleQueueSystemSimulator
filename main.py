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
            python3 main.py [minArrive] [maxArrive] [minExit] [maxExit] [n] [capacity] [servers]
            
            Glossary:

            minArrive ->
            maxArrive ->
            minExit   ->
            maxExit   ->
            n         ->
            capacity  ->
            servers   ->
            """

"""
TODO: 
    - Ler arquivo de entrada (cuidar criação do Producer() na classe Simulator())
    - Permitir a leitura de uma sequência de 'aleatórios' previamente calculados
    - Verificar se o report está OK (bater com a classe disponibilizada pelo professor)
"""

if __name__ == '__main__':
    
    tprint("Queue simulator", font="cybermedium")
    
    args = argv
    if args[1] == 'teacher':
        root = tk.Tk()
        d = display.Display(master=root)
        d.mainloop()
    
    elif args[1] == 'help':
        print(help)

    else:
        try:
            args = [int(i) for i in args if i.isnumeric()]
            Simulator(minArrive=args[0], maxArrive=args[1], \
                        minExit=args[2], maxExit=args[3], \
                        n=args[4], capacity=args[5], servers=args[6] \
                    ).init(3)

        except Exception as e:
            print(e)
            print(help)
