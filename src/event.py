#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in dependencies
from enum import Enum


class EventType(Enum):

    """
    - Event type abstraction
    - Types:
        - Arrive
        - Transition
        - Departure
    """

    arrive = 1
    transition = 2
    departure = 3

class Event: 

    """
    - Representation of an event in the queue
    - Methods
        - __init__(type, time)
    """

    def __init__(self, source:int, target:int, type:EventType, time:float) -> None:
        self.source = source
        self.target = target
        self.type = type
        self.time = time

    def __repr__(self) -> str:
        return f"source={self.source} target={self.target} type={self.type} time={self.time}"
