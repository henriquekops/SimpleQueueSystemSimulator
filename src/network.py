#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.queue import Queue
from src.utils.config import YamlParser

class Network:

    __OBJ = 'object'
    __TGT = 'targets'

    def __init__(self, yml_data: YamlParser) -> None:
        self.__network = dict()
        self.__builder(yml_data)

    def add(self, id:int, queue:Queue) -> None:
        """
        Add new queue to network
        """
        self.__network[id] = dict()
        self.__network[id][self.__OBJ] = queue
        self.__network[id][self.__TGT] = dict()

    def chain(self, source:int, target:int, weight:float=1.0) -> None:
        """
        Chain queues with weighted paths 
        """
        # *TODO: when sum of weights != 1.0, we MAY need to keep track of 'outer' weights (see example below) 
        self.__network[source][self.__TGT][target] = weight

    def queue(self, id:int) -> Queue:
        """
        Retrieve the queue for input id
        """
        return self.__network[id][self.__OBJ]

    def targets(self, id:int) -> dict():
        """
        Retrieve targets for input id 
        """
        return self.__network[id][self.__TGT]
    
    def __builder(self, yml_data):
        
        for queue in yml_data['queues']:
            print(queue)
            queue_aux = Queue(capacity=queue['capacity'], 
                              servers=queue['servers'], 
                              minArrival=queue['minArrival'], 
                              maxArrival=queue['maxArrival'], 
                              minExit=queue['minExit'], 
                              maxExit=queue['maxExit'])
            
            id = yml_data['queues'].index(queue) + 1
            self.add(id=id, queue=queue)
            
        for queue_net in yml_data['network']:
            self.chain(source=queue_net['source'], target=queue_net['target'], weight=queue_net['weight'])
    
    def show(self):
        for k, v in self.__network.items():
            print(f"{k} : {v} \n")
    

# Example of this network

# {
#     1: {
#         'object': Queue(),
#         'targets': {
#             2: 1.0
#         }
#     },
#     2: {
#         'object': Queue(),
#         'targets': {
#             0: 0.5,       -> '0' means 'out' (*TODO: generate this value whenever sum of targets != 1.0)
#             1: 0.5
#         }
#     }
# }
