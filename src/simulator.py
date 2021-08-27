#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.queue import Queue
from src.scheduler import Scheduler
from src.producer import Producer
from src.event import (
    Event,
    EventType
)


class Simulator:

    """
    - Simulator controls the simulation workflow
    - Methods:
        - __init__(start)
    """

    # TODO: read random list for testing

    def __init__(self, minArrive:int, maxArrive:int, minExit:int, maxExit:int, n:int):
        self.__n = n
        self.__global_time = 0
        self.__minArrive = minArrive
        self.__maxArrive = maxArrive
        self.__minExit = minExit
        self.__maxExit = maxExit
        self.__queue = Queue()
        self.__scheduler = Scheduler()
        self.__producer = Producer()

    def init(self, start:int):
        self.__scheduler(Event(type=EventType.arrive, time=(start)))
        while(self.__n > 0):
            # TODO: check for loop finish (self.__n)
            event: Event = self.__scheduler.next()
            if event.type == EventType.arrive:
                self.__arrive(event.time)
            elif event.type == EventType.exit:
                self.__departure(event.time)
            else:
                print('Not implemented yet (transition)')

    def __arrive(self, time:float) -> None:
        delta = time - self.__global_time
        self.__global_time = time
        self.__queue.update_queue_time(delta)
        if self.__queue.is_slot_available():
            self.__queue.enter()
            if self.__queue.is_server_available():
                r = self.__producer.generate(self.__minExit, self.__maxExit)
                self.__scheduler.add(Event(type=EventType.departure, time=(self.__global_time + r)))
                self.__n -= 1
        r = self.__producer.generate(self.__minArrive, self.__maxArrive)
        self.__scheduler(Event(type=EventType.arrive, time=(self.__global_time + r)))
        self.__n -= 1

    def __departure(self, time:float):
        delta = time - self.__global_time
        self.__global_time = time
        self.__queue.update_queue_time(delta)
        self.__queue.exit()
        if self.__queue.was_someone_waiting():
            r = self.__producer.generate(self.__minExit, self.__maxExit)
            self.__scheduler(Event(type=EventType.departure, time=(self.__global_time + r)))
            self.__n -= 1
