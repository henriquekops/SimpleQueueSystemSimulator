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

    def __init__(self, minArrive:int, maxArrive:int, minExit:int, maxExit:int, n:int, capacity:int, servers:int):
        self.__n = n
        self.__global_time = 0
        self.__minArrive = minArrive
        self.__maxArrive = maxArrive
        self.__minExit = minExit
        self.__maxExit = maxExit
        self.__queue = Queue(capacity=capacity, servers=servers)
        self.__scheduler = Scheduler()
        self.__producer = Producer(x=7, a=4, c=4, m=9)
        self.__event_id = 0

    def init(self, start:int):
        self.__scheduler.add(Event(type=EventType.arrive, time=(start), id=self.__event_id))
        self.__event_id += 1
        while(self.__n > 0):
            # TODO: check for loop finish (self.__n)
            event: Event = self.__scheduler.next()[1]
            print(f'[ Event incoming: time={event.time} type={event.type} id={event.id} ]')
            if event.type == EventType.arrive:
                self.__arrive(event)
            elif event.type == EventType.departure:
                self.__departure(event)
            else:
                print('Not implemented yet (transition)')
        print(f'Simulation ended, report:\n{self.__queue.results(self.__global_time)}')

    def __arrive(self, event:Event) -> None:
        delta = event.time - self.__global_time
        self.__global_time = event.time
        self.__queue.update_queue_time(delta)
        if self.__queue.is_slot_available():
            print(f'[{event.id}] Entered Queue!')
            self.__queue.enter()
            if self.__queue.is_server_available():
                r = self.__producer.generate(self.__minExit, self.__maxExit)
                self.__scheduler.add(Event(type=EventType.departure, time=(self.__global_time + r), id=self.__event_id))
                self.__event_id += 1
                print(f'[{event.id}] Im being attended, will leave at: {self.__global_time + r}')
                self.__n -= 1
        else:
            print(f'[{event.id}] Queue is full, im leaving...')
        r = self.__producer.generate(self.__minArrive, self.__maxArrive)
        self.__scheduler.add(Event(type=EventType.arrive, time=(self.__global_time + r), id=self.__event_id))
        self.__event_id += 1
        self.__n -= 1

    def __departure(self, event:Event):
        delta = event.time - self.__global_time
        self.__global_time = event.time
        self.__queue.update_queue_time(delta)
        self.__queue.exit()
        print(f'[{event.id}] Leaving queue!')
        if self.__queue.was_someone_waiting():
            r = self.__producer.generate(self.__minExit, self.__maxExit)
            self.__scheduler.add(Event(type=EventType.departure, time=(self.__global_time + r), id=self.__event_id))
            self.__event_id += 1
            print(f'[{event.id}] Letting next come, it will leave at: {self.__global_time + r}')
            self.__n -= 1
