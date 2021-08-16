#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue:

    def __init__(self, size=None) -> None:

        self.size = size
        self.servers = None
        self.check_in = list()
        self.treatment = list()
        self.data = list()
    
    def _set_time(self, target) -> None:
        """
        Set to target the current time thats was called

        Parameters:
            targer:
                check_in or tratment
        
        Return: None
        """
        pass

    def set_servers(self, list_servers) -> None:
        """
        Add a list of server on queue server atribute

        Parameters:
            list_servers
        
        Return: None
        """
        pass

    def handle(self, random_number) -> bool:
        """
        Process the numbers

        Parameters:
            random_number
        
        Return: bool
        """
        self._set_time()
        pass
    

