#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.queue import Queue
from src.scheduler import Scheduler
from src.producer import Producer
from src.event import (
    Event,
    EventType
)

# built-in dependencies
from typing import List
from enum import Enum

class SimulationType(Enum):
    
    simple = 1
    tandem = 2


class Simulator:

    """
    - Simulator controls the simulation workflow
    - Methods:
        - init(start, capacities, servers, minArrivals, maxArrivals, minExits, maxExits)
        - __arrive(event, simulation_type)
        - __departure(event)
        - __transition(event)
        - __start_queues(capacities, servers)
        - __schedule(type, min, max)
        - __compute_time(event)
    """

    # TODO: read random list for testing
    
    X = 3
    A = 33
    C = 11
    M = 2147483643

    def __init__(self, n:int, use_loss):
        self.__n = n
        self.__global_time = 0
        self.__queues = []
        self.__scheduler = Scheduler()
        self.__producer = Producer(x=self.X, a=self.A, c=self.C, m=self.M)
        self.__use_loss = use_loss
        self.__loss = 0

    def init(self, start:int, capacities:List, servers:List, minArrivals:List, maxArrivals:List, minExits:List, maxExits:List):        
        self.__start_queues(capacities, servers, minArrivals, maxArrivals, minExits, maxExits)
        self.__scheduler.add(Event(type=EventType.arrive, time=(start)))
        
        while(self.__n > 0):
            event:Event = self.__scheduler.next()[1]
            if event.type == EventType.arrive:
                self.__arrive(event, SimulationType.tandem) # TODO: drop hard coded
            elif event.type == EventType.departure:
                self.__departure(event)
            elif event.type == EventType.transition:
                self.__transition(event)
        
        queue:Queue
        for queue in self.__queues:
            print(f'\nSimulation ended for queue {self.__queues.index(queue)}:\n{queue.results(self.__global_time)}\n')

    def __arrive(self, event:Event, simulation_type:SimulationType) -> None:
        self.__compute_time(event)
        first_queue:Queue = self.__queues[0]  # TODO: How do i know which queue is the first?
        if first_queue.is_slot_available():
            first_queue.enter()
            if first_queue.is_server_available():
                if simulation_type == SimulationType.simple:
                    self.__schedule(EventType.departure, first_queue.minExit, first_queue.maxExit)
                elif simulation_type == SimulationType.tandem:
                    self.__schedule(EventType.transition, first_queue.minExit, first_queue.maxExit)
        else:
            if self.__use_loss:
                self.__loss += 1
        self.__schedule(EventType.arrive, first_queue.minArrival, first_queue.maxArrival)

    def __departure(self, event:Event):
        self.__compute_time(event)
        last_queue:Queue = self.__queues[-1] # TODO: How do i know which queue is the last?
        last_queue.exit()
        if last_queue.was_someone_waiting():
            self.__schedule(EventType.departure, last_queue.minExit, last_queue.maxExit)

    def __transition(self, event: Event):
        self.__compute_time(event)
        queue_1:Queue = self.__queues[0] # TODO: how do i know from where events are transitioning
        queue_2:Queue = self.__queues[1] # TODO: how do i know to where events are transitioning
        queue_1.exit()
        if queue_1.was_someone_waiting():
            self.__schedule(EventType.transition, queue_1.minExit, queue_1.maxExit)
            
        if queue_2.is_slot_available():
            queue_2.enter()
            if queue_2.is_server_available():
                self.__schedule(EventType.departure, queue_2.minExit, queue_2.maxExit)
                
        else:
            if self.__use_loss:
                self.__loss += 1
                

    def __start_queues(self, capacities:List, servers:List, minArrivals:List, maxArrivals:List, minExits:List, maxExits:List) -> None:
        for c, s, min_a, max_a, min_e, max_e in zip(capacities, servers, minArrivals, maxArrivals, minExits, maxExits):
            self.__queues.append(Queue(c, s, min_a, max_a, min_e, max_e))

    def __schedule(self, event_type:EventType, min:int, max:int):
        r = self.__producer.generate(min, max)
        self.__scheduler.add(Event(type=event_type, time=(self.__global_time + r)))
        self.__n -= 1

    def __compute_time(self, event:Event) -> None:
        delta = event.time - self.__global_time
        self.__global_time = event.time
        queue: Queue
        for queue in self.__queues:
            queue.update_queue_time(delta) 
