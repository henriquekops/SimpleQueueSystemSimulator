#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import json
from src.utils.config import YamlParser
from configparser import ConfigParser
from sys import argv
from art import tprint
from src.simulator import Simulator
from src.network import Network
from src.ui import (
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
    p = YamlParser()    
    is_valid, err = p.validate('examples/example.yaml')
    
    if is_valid:

        yml_data = p.read('examples/example.yaml')
        for k, v in yml_data.items():
            print(f"{k} : {v} \n")
    
        net = Network(yml_data=yml_data)
        print(net)
    
    else:
        print(err)
    
#    conf = ConfigParser()
#    conf.read('setup.cfg')
#
#    tprint("Queue simulator", font="cybermedium")
#    
#    args = argv
#
#
#    try:
#        if args[1] == 'teacher':
#            root = tk.Tk()
#            d = display.Display(master=root)
#            d.mainloop()
#    except:
#       pass
#
#    Simulator(
#            n=int(conf.get('Queue','n')), 
#            use_loss=bool(conf.get('Queue','use_loss'))
#        ).init(
#            start=int(conf.get('Queue','start')),
#            capacities=[int(x) for x in json.loads(conf.get('Queue','capacities'))],
#            servers=[int(x) for x in json.loads(conf.get('Queue','servers'))],
#            minArrivals=[int(x) for x in json.loads(conf.get('Queue','minArrivals'))],
#            maxArrivals=[int(x) for x in json.loads(conf.get('Queue','maxArrivals'))],
#            minExits=[int(x) for x in json.loads(conf.get('Queue','minExits'))],
#            maxExits=[int(x) for x in json.loads(conf.get('Queue','maxExits'))]
#        )
