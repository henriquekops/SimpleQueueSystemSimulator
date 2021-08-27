#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    """
    - Responsible for simulating queue
    - Methods:
        - __init__(capacity, servers)
        - is_slot_available()
        - is_server_available()
        - was_someone_waiting()
        - enter()
        - exit()
        - update_queue_time(time)
        - results(global_time)
    """

    def __init__(self, capacity:int, servers:int) -> None:
        self.__times = [0.0] * ( capacity + 1 ) # TODO: when infinite??
        self.__capacity = capacity
        self.__servers = servers
        self.__loss = 0
        self.__position = 0

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
        f""" 
            Capacity: {self.__capacity}
            Servers: {self.__servers}
            Loss: {self.__loss}
            Times: {self.__times}
            Percents: {[( t / global_time ) for t in self.__times]}
        """}
