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

    if len(argv) != 2:
        print(HELP)
        exit(0)

    yml = argv[1]

    if not exists(yml):
        print(f"File '{yml}' not found!")
        exit(0)

    parser = YamlParser()
    is_valid, err = parser.validate(yml)
    
    if is_valid:

        yml_data = parser.read(yml)

        producer = Producer(yml_data=yml_data.get('pseudo_random_generation'))
        network = Network(yml_data=yml_data.get('network'))

        # TODO: what about 'inputs' field?
        yml_control = yml_data.get('control')
        simulator = Simulator(yml_control.get('n'), yml_control.get('use_loss'), network, producer)
        simulator.start(yml_control.get('start'))
    
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
