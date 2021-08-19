#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    """
    - Responsible for simulating queue
    - Methods:
        - set_servers(server_list)
        - handle(time)
    """

    def __init__(self, capacity:int, servers:int) -> None:
        self.__capacity = capacity
        self.__servers = servers
        self.__loss = 0
        self.__serving = 0

    def is_full(self) -> bool:
        return self.__serving == self.__capacity

    def is_next(self) -> bool:
        return self.__serving <= 1

    def is_empty(self) -> bool:
        return self.__serving == 0

    def arrive(self) -> None:
        self.__serving += 1

    def exit(self) -> None:
        self.__serving -= 1

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

        return
    

