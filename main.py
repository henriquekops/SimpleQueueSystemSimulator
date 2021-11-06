#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from sys import (
    argv,
    exit
)
from os.path import exists
from os import system

# project dependencies
from src.utils.config import YamlParser
from src.simulator import Simulator
from src.network import Network
from src.producer import Producer

# external dependencies
from art import tprint


HELP =  """Run:\n\tpython3 main.py <your-setup>.yaml\nExample:\n\tpython3 main.py example"""

"""
TODO:
    - Permitir a leitura de uma sequência de 'aleatórios' previamente calculados
"""

if __name__ == '__main__':
    
    tprint("Queue simulator", font="cybermedium")

    if len(argv) != 2:
       print(HELP)
       exit(0)

    cmd = argv[1]

    if cmd == "example":
        system("cat examples/example.yaml")
        exit(0)

    yml = cmd

    if not exists(yml):
        print(f"File '{yml}' not found!")
        exit(0)

    parser = YamlParser()
    is_valid, err = parser.validate(yml)
    
    if is_valid:

        yml_data = parser.read(yml)

        producer = Producer(yml_data=yml_data.get('pseudo_random_generation'))
        network = Network(yml_data=yml_data)

        yml_control = yml_data.get('control')
        simulator = Simulator(yml_control.get('n'), network, producer)
        simulator.init(yml_control.get('inputs'))
    
    else:
        print(err)


# TODO: Recreate UI
# root = tk.Tk()
#            d = display.Display(master=root)
#            d.mainloop()
