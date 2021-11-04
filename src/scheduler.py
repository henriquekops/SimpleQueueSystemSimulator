#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Tuple
from heapq import (
    heappop,
    heappush
)
from src.event import Event

class Scheduler:

    """
    - Min-heap representation using b-tree for random event scheduling
    - Methods:
        - __init__()
        - add(element)
        - next()
    """

    def __init__(self) -> None:
        self.__heap = []

    def add(self, element: Event) -> None:
        """
        - Insert element at heap
        - Params:
            - element: Element to be inserted 
        - Returns:
            - None
        """
        heappush(self.__heap, (element.time, element))

    def next(self) -> Tuple[float, Event]:
        """
        - Give next client at min heap
        - Params:
            - None
        - Returns:
            - None
        """
        e =  heappop(self.__heap)
        print(e)
        return e
