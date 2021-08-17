#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import (
    heapify,
    heappop,
    heappush
)

class Scheduler:

    """
    - Min-heap representation using b-tree for random event scheduling
    - Methods:
        - __init__()
        - add()
        - next()
    """

    def __init__(self) -> None:
        self.__heap = []

    def add(self, element):
        """
        - Insert element at heap
        - Params:
            - element: Element to be inserted 
        - Returns:
            - None
        """
        heappush(self.__heap, element)

    def next(self):
        """
        - Give next client at min heap
        - Params:
            - None
        - Returns:
            - None
        """
        return heappop(self.__heap)
