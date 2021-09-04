#!/usr/bin/env python
# -*- coding: utf-8 -*-

from art import tprint
import tkinter as tk
from src.simulator import Simulator
from src import (
    display
)

"""
TODO: 
    - Ler arquivo de entrada (cuidar criação do Producer() na classe Simulator())
    - Permitir a leitura de uma sequência de 'aleatórios' previamente calculados
    - Verificar se o report está OK (bater com a classe disponibilizada pelo professor)
"""

if __name__ == '__main__':
    tprint("Queue simulator", font="cybermedium")
    # root = tk.Tk()
    # d = display.Display(master=root)
    # d.mainloop()
    
    Simulator(minArrive=1, maxArrive=2, minExit=3, maxExit=6, n=10, capacity=3, servers=1).init(2)

