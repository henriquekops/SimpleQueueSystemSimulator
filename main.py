#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import (
    producer,
    display
)

if __name__ == '__main__':
    p = producer.Producer(7)
    seq = p.generate(4, 4, 9, 100)
    d = display.Display()
    d.plot(seq)
