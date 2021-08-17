#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Producer:

    """
    - Producer:
        - Generates a sequence of random numbers using linear congruent method
    - Methods:
        - __init__()
        - generate(a, c, m)
    """
    
    def __next(self, x:int, a:int, c:int, m:int) -> int:
        """
        - Params:
            - x: seed to consider
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
        - Returns:
            - Next random value in sequence
        """
        return ((a * x) + c) % m

    def generate(self, x:int, a:int, c:int, m:int, n:int) -> List[int]:
        """
        - Params:
            - x: seed to start random sequence
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
            - n: size of sequence
        - Returns:
            - Random integer sequence based on initial seed and params
        """
        lst = []
        for _ in range (n):
            x = self.__next(x, a, c, m)
            lst.append(x)
        return lst
