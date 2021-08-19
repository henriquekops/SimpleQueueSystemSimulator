#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Producer:

    """
    - Generates a sequence of random numbers using linear congruent method
    - Methods:
        - __init__(x, a, c, m, n)
        - generate() 
    """

    def __init__(self, x:int, a:int, c:int, m:int, n:int):
        """
        Params:
            - x: seed to start random sequence
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max random value in sequence
            - n: size of sequence
        """
        self.__x = x
        self.__a = a
        self.__c = c
        self.__m = m
        self.__n = n

    def __next(self, x) -> int:
        """
        - Computes next number in random sequence
        - Params:
            - x: seed to generate the random value
        - Returns:
            - Next random value in sequence
        """
        
        return ((self.__a * x) + self.__c) % self.__m

    def __normalize(self, x:int) -> float:
        """
        - Normalizes the random number at the interval [0;1)
        - Param:
            - x: random value previously generated
        - Returns:
            - Normalized random number 
        """
        
        return round(x / self.__m, 2)

    def __get_at_interval(self, n_x:int, a:int, b:int):
        """
        - Find normalized random value inside an interval
        - Params:
            - n_x: normalized random value previously generated
            - a: interval start
            - b: interval end
        """
        return (b - a) * n_x

    def generate(self, a, b) -> List[float]:
        """
        - Generates random sequence using linear congruent method
        - Params:
            - a: interval start
            - b: interval end
        - Returns:
            - Random float sequence based on seed and params
        """
        lst = []
        x = self.__x
        for i in range (self.__n):
            x = self.__next(x)
            n_x = self.__normalize(x)
            lst.append(self.__get_at_interval(n_x, a, b))
        return lst
