#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class EventType(Enum):
    arrive = 1
    transition = 2
    exit = 3

class Event:

    # TODO: time is global 

    def __init__(self, type:EventType, time:float) -> None:
        self.type = -1
        self.time = -1
