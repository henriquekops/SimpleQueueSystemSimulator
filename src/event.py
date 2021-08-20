#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class EventType(Enum):
    arrive = 1
    transition = 2
    departure = 3

class Event: 

    def __init__(self, type:EventType, time:float) -> None:
        self.type = type
        self.time = time
