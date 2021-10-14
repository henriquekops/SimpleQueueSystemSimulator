#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def __init__(self, type:EventType, time:float) -> None:
        self.type = type
        self.time = time
