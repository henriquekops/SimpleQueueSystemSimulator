#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project dependencies
from src.network import Network
from src.queue import Queue
from src.scheduler import Scheduler
from src.producer import Producer
from src.event import (
    Event,
    EventType
)

# built-in dependencies
from random import choices


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
    
    def __init__(self, n:int, network:Network, producer:Producer):
        self.__n = n
        self.__network = network
        self.__global_time = 0
        self.__scheduler = Scheduler()
        self.__producer = producer

    def init(self, inputs):
        for input in inputs:
            event = Event(
                source=0,
                target=input.get('queue'),
                type=EventType.arrive,
                time=float(input.get('start'))
            )
            self.__scheduler.add(event)
        
        while(self.__n > 0):
            event:Event = self.__scheduler.next()[1]
            if event.type == EventType.arrive:
                self.__arrive(event)
            elif event.type == EventType.departure:
                self.__departure(event)
            elif event.type == EventType.transition:
                self.__transition(event)
        
        queue: Queue
        for queue in self.__network.queues():
            queue.results(self.__global_time)

    def __arrive(self, event:Event) -> None:
        self.__compute_time(event)
        queue = self.__network.queue(event.target)
        if queue.is_slot_available():
            queue.enter()
            if queue.is_server_available():
                targets = self.__network.targets(queue.id)
                queue_id = self.__choose_path(targets)
                if queue_id == 0:
                    self.__schedule(
                        source=event.target,
                        target=0,
                        event_type=EventType.departure,
                        min=queue.minExit,
                        max=queue.maxExit
                    )
                else:
                    self.__schedule(
                        source=event.target,
                        target=queue_id,
                        event_type=EventType.transition,
                        min=queue.minExit,
                        max=queue.maxExit
                    )
        else:
            queue.loss += 1
        self.__schedule(
            source=0,
            target=event.target,
            event_type=EventType.arrive,
            min=queue.minArrival,
            max=queue.maxArrival
        )

    def __departure(self, event:Event):
        self.__compute_time(event)
        queue = self.__network.queue(event.source)
        queue.exit()
        if queue.was_someone_waiting():
            targets = self.__network.targets(queue.id)
            queue_id = self.__choose_path(targets)
            if queue_id == 0:
                self.__schedule(
                    source=event.source,
                    target=0,
                    event_type=EventType.departure,
                    min=queue.minExit,
                    max=queue.maxExit
                )
            else:
                self.__schedule(
                    source=event.source,
                    target=queue_id,
                    event_type=EventType.transition,
                    min=queue.minExit,
                    max=queue.maxExit
                )

    def __transition(self, event: Event):
        self.__compute_time(event)
        queue_1 = self.__network.queue(event.source)
        queue_2 = self.__network.queue(event.target)
        queue_1.exit()
        if queue_1.was_someone_waiting():
            targets = self.__network.targets(queue_1.id) 
            queue_id = self.__choose_path(targets)
            if queue_id == 0:
                self.__schedule(
                    source=event.source,
                    target=0,
                    event_type=EventType.departure,
                    min=queue_1.minExit,
                    max=queue_1.maxExit
                )
            else:
                self.__schedule(
                    source=event.source,
                    target=queue_id,
                    event_type=EventType.transition,
                    min=queue_1.minExit,
                    max=queue_1.maxExit
                )
        if queue_2.is_slot_available():
            queue_2.enter()
            if queue_2.is_server_available():
                targets = self.__network.targets(queue_2.id)
                queue_id = self.__choose_path(targets)
                if queue_id == 0:
                    self.__schedule(
                        source=event.target,
                        target=0,
                        event_type=EventType.departure,
                        min=queue_2.minExit,
                        max=queue_2.maxExit
                    )
                else:
                    self.__schedule(
                        source=event.target,
                        target=queue_id,
                        event_type=EventType.transition,
                        min=queue_2.minExit,
                        max=queue_2.maxExit
                    )
        else:
            queue_2.loss += 1

    def __schedule(self, source:int, target:int, event_type:EventType, min:float, max:float):
        r = self.__producer.generate(min, max)
        self.__scheduler.add(
            Event(
                source=source,
                target=target,
                type=event_type,
                time=(self.__global_time + r)
            )
        )
        self.__n -= 1

    def __compute_time(self, event:Event) -> None:
        delta = event.time - self.__global_time
        self.__global_time = event.time
        queue: Queue
        for queue in self.__network.queues():
            queue.update_queue_time(delta) 

    def __choose_path(self, targets:dict) -> Queue: # TODO: Consume random number
        # self.__n -= 1
        return choices(
            population=list(targets.keys()),
            weights=list(targets.values()),
            k=1
        )[0]
