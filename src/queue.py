#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Queue:

    """
    - Responsible for simulating queue
    - Methods:
        - __init__(capacity, servers, minArrival, maxArrival, minExit, maxExit)
        - is_slot_available()
        - is_server_available()
        - was_someone_waiting()
        - enter()
        - exit()
        - update_queue_time(time)
        - results(global_time)
    """

    def __init__(self, capacity:int=0, servers:int=0, minArrival:int=0, maxArrival:int=0, minExit:int=0, maxExit:int=0) -> None:
        self.__times = []
        self.__capacity = capacity
        self.__servers = servers
        self.minArrival = minArrival
        self.maxArrival = maxArrival
        self.minExit = minExit
        self.maxExit = maxExit
        self.__loss = 0
        self.__position = 0

    def __repr__(self):
        return str({
            "capacity": self.__capacity,
            "servers": self.__servers,
            "minArrival": self.minArrival,
            "maxArrival": self.minArrival,
            "minExit": self.minExit,
            "maxExit": self.maxExit
        })

    def is_slot_available(self) -> bool:
        return self.__position < self.__capacity

    def is_server_available(self) -> bool:
        return self.__position <= self.__servers

    def was_someone_waiting(self) -> bool:
        return self.__position >= self.__servers

    def enter(self) -> None:
        self.__position += 1

    def exit(self) -> None:
        self.__position -= 1

    def update_queue_time(self, time:float) -> None:
        self.__times[self.__position] += time

    def results(self, global_time:float) -> str:
        return {
            "capacity": self.__capacity,
            "servers": self.__servers,
            "loss": self.__loss,
            "times": self.__times,
            "percents": [( t / global_time ) for t in self.__times]
        }
