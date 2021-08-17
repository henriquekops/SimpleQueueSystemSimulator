#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Producer:

    """
    - Generates a sequence of random numbers using linear congruent method
    - Methods:
        - __init__()
        - generate(x, a, c, m, n) 
    """
    
    def __next(self, x:int, a:int, c:int, m:int) -> int:
        """
        - Computes next number in random sequence
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
        - Generates random sequence using linear congruent method
        - Params:
            - x: seed to start random sequence
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
            - n: size of sequence
        - Returns:
            - Random integer sequence based on seed and params
        """
        lst = []
        for _ in range (n):
            x = self.__next(x, a, c, m)
            lst.append(x)
        return lst
