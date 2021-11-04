#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from sys import (
    argv,
    exit
)
from os.path import exists

# project dependencies
from src.utils.config import YamlParser
from src.simulator import Simulator
from src.network import Network
from src.producer import Producer

# external dependencies
from art import tprint


HELP =  """ Run:\n\tpython3 main.py <your-setup>.yaml\nGenerate:\n\t<TBD>"""


"""
TODO: 
    - Ler arquivo de entrada (cuidar criação do Producer() na classe Simulator())
    - Permitir a leitura de uma sequência de 'aleatórios' previamente calculados
"""

if __name__ == '__main__':
    
    tprint("Queue simulator", font="cybermedium")

    #if len(argv) != 2:
    #    print(HELP)
    #    exit(0)

    yml = 'examples/example.yaml'#argv[1]

    if not exists(yml):
        print(f"File '{yml}' not found!")
        exit(0)

    parser = YamlParser()
    is_valid, err = parser.validate(yml)
    
    if is_valid:

        yml_data = parser.read(yml)

        producer = Producer(yml_data=yml_data.get('pseudo_random_generation'))
        network = Network(yml_data=yml_data)

        # TODO: pass 'inputs' to simulator
        yml_control = yml_data.get('control')
        simulator = Simulator(yml_control.get('n'), network, producer)
        print(yml_control.get('start'))
        simulator.init(yml_control.get('inputs'))
    
    else:
        print(err)


# TODO: Recreate UI
# root = tk.Tk()
#            d = display.Display(master=root)
#            d.mainloop()
