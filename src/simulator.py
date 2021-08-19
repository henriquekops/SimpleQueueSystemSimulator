#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.queue import Queue
from src.scheduler import Scheduler
from src.producer import Producer


class Simulator:

    """
    - Simulator controls the simulation workflow
    - Methods:
        - __init__(start) 
    """

    def __init__(self, start:int, minArrive:int, maxArrive:int, minExit:int, maxExit:int):
        self.__global_time = start
        self.__minArrive = minArrive
        self.__maxArrive = maxArrive
        self.__minExit = minExit
        self.__maxExit = maxExit
        self.__queue = Queue()
        self.__scheduler = Scheduler()
        self.__producer = Producer()
        self.__random_sequence = self.__producer.generate()

    def arrive(self) -> None:
        # contabiliza tempo ?
        if not self.__queue.is_full:
            self.__queue.arrive()
            if self.__queue.is_next():
                r = self.__producer.generate(self.__minExit, self.__maxExit)
                self.__scheduler.add(self.__global_time + r)
        r = self.__producer.generate(self.__minArrive, self.__maxArrive)
        self.__scheduler(self.__global_time + r)

    def exit(self):
        # contabiliza tempo ?
        self.__queue.exit()
        if not self.__queue.is_empty():
            r = self.__producer.generate(self.__minExit, self.__maxExit)
            self.__scheduler(self.__global_time + r)

