#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    """
    - Responsible for simulating queue
    - Methods:
        - set_servers(server_list)
        - handle(time)
    """

    def __init__(self, capacity:int, servers:int, minArrival:int, maxArrival:int, minServe:int, maxServe:int) -> None:
        self.__capacity = capacity
        self.__servers = servers
        self.__minArrival = minArrival
        self.__maxArrival = maxArrival
        self.__minServe = minServe
        self.__maxServe = maxServe
        self.__loss = 0
    
    def _set_global_time(self, increment) -> None:
        """
        - Increase the simulation's global time 
        - Parameters:
            - increment: Increase global time
        - Returns:
            - None
        """
        pass

    def set_servers(self, server_list) -> None:
        """
        - Add servers to serve clients
        - Parameters:
            - server_list: List of servers 
        - Returns:
            - None
        """
        pass

    def handle(self, time) -> bool:
        """
        - Serve client
        - Parameters:
            - time: Time needed to serve client
        - Returns:
            - Boolean if finished serving
        """
        self._set_time()
        pass
    

