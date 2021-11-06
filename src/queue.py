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

    def __init__(self, id:int, capacity:int=0, servers:int=0, minArrival:int=0, maxArrival:int=0, minExit:int=0, maxExit:int=0) -> None:
        self.__capacity = capacity if capacity else 0
        self.minArrival = minArrival if minArrival else 0.0
        self.maxArrival = maxArrival if maxArrival else 0.0
        
        if self.__capacity > 0:
            self.__times = [0.0] * self.__capacity
        else:
            self.__times = [0.0]
        
        self.id = id
        self.__servers = servers
        self.minExit = minExit
        self.maxExit = maxExit
        self.loss = 0
        self.__position = 0

    def __repr__(self):
        return str({
            "id": self.id,
            "capacity": self.__capacity,
            "servers": self.__servers,
            "minArrival": self.minArrival,
            "maxArrival": self.minArrival,
            "minExit": self.minExit,
            "maxExit": self.maxExit
        })

    def is_slot_available(self) -> bool:
        if self.__capacity > 0:
            return self.__position < self.__capacity-1
        else:
            return True # infinite queue

    def is_server_available(self) -> bool:
        return self.__position <= self.__servers

    def was_someone_waiting(self) -> bool:
        return self.__position >= self.__servers

    def enter(self) -> None:
        self.__position += 1

    def exit(self) -> None:
        self.__position -= 1

    def update_queue_time(self, time:float) -> None:
        if self.__capacity == 0:
            if len(self.__times) < self.__position+1:
                self.__times.append(0.0)
            
        self.__times[self.__position] += time

    def results(self, global_time:float) -> str:
        return f"Results for queue {self.id}:\n" + str({
            "capacity": self.__capacity,
            "servers": self.__servers,
            "loss": self.loss,
            "times": self.__times,
            "percents": [( t / global_time ) for t in self.__times]
        })
