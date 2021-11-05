#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from typing import List

# project dependencies
from src.queue import Queue


class Network:

    # Example of this network
    #
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
    #             0: 0.5,
    #             1: 0.5
    #         }
    #     }
    # }

    __OBJ = 'object'
    __TGT = 'targets'

    def __init__(self, yml_data: dict) -> None:
        self.__network = dict()
        self.__builder(yml_data)

    def __repr__(self) -> str:
        """
        To string
        """
        return self.__network.__str__()

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
        self.__network[source][self.__TGT][target] = weight

    def queue(self, id:int) -> Queue:
        """
        Retrieve the queue for input id
        """
        return self.__network[id][self.__OBJ]

    def targets(self, id:int) -> dict:
        """
        Retrieve targets for input id 
        """
        return self.__network[id][self.__TGT]
    
    def queues(self) -> List[Queue]:
        """
        Retrieve all queues from network
        """
        return [q[self.__OBJ] for q in self.__network.values()]

    def __builder(self, yml_data: dict):
        id = 0
        for yml_queue in yml_data['queues']:
            id += 1
            self.add(
                id=id,
                queue=Queue(
                    id=id,
                    capacity=yml_queue.get('capacity'), 
                    servers=yml_queue.get('servers'), 
                    minArrival=yml_queue.get('minArrival'), 
                    maxArrival=yml_queue.get('maxArrival'), 
                    minExit=yml_queue.get('minExit'), 
                    maxExit=yml_queue.get('maxExit')
                )
            )
        for queue_net in yml_data['network']:
            self.chain(
                source=queue_net['source'],
                target=queue_net['target'],
                weight=queue_net['weight']
            )

        for queue in self.__network.values():
            s = sum(queue[self.__TGT].values())
            if s < 1.0:
                queue[self.__TGT][0] = 1 - s
