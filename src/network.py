#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from queue import Queue

class Network:

    __OBJ = 'object'
    __TGT = 'targets'

    def __init__(self) -> None:
        self.__network = dict()

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
