#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    """
    - Responsible for simulating queue
    - Methods:
        - set_servers(server_list)
        - handle(time)
    """

    def __init__(self, size=None) -> None:
        self.size = size
        self.servers = None
        self.check_in = list()
        self.treatment = list()
        self.data = list()
    
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
    

