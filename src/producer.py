#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import overload

class Producer:

    """
    - Generates a sequence of random numbers using linear congruent method
    - Methods:
        - __init__(x, a, c, m, n)
        - generate() 
    """

    def __init__(self, x:int = 0, a:int = 0, c:int = 0, m:int = 0):
        """
        Params:
            - x: seed to start random sequence
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max random value in sequence
        """
        
        self.__x = x
        self.__a = a
        self.__c = c
        self.__m = m

    def __next(self, prev_x) -> int:
        """
        - Computes next number in random sequence
        - Params:
            - x: seed to generate the random value
        - Returns:
            - Next random value in sequence
        """
        
        return ((self.__a * prev_x) + self.__c) % self.__m

    def __normalize(self, x:int) -> float:
        """
        - Normalizes the random number at the interval [0;1)
        - Param:
            - x: random value previously generated
        - Returns:
            - Normalized random number 
        """
        
        return x / self.__m

    def __get_at_interval(self, n_x:int, a:int, b:int) -> float:
        """
        - Find normalized random value inside an interval
        - Params:
            - n_x: normalized random value previously generated
            - a: interval start
            - b: interval end
        - Returns:
            - Random normalized value inside interval
        """

        return ( (b - a) * n_x ) + a

    def generate(self, a, b) -> float:
        """
        - Generates random sequence using linear congruent method
        - Params:
            - a: interval start
            - b: interval end
        - Returns:
            - Random float sequence based on seed and params
        """

        self.__x = self.__next(self.__x)
        return self.__get_at_interval(self.__normalize(self.__x), a, b)

    def generate2(self) -> float:
        """
        - Generate next pseudo random value in sequence 
        - Returns:
            - Next random sequence value at interval [0;1)
        """
        
        self.__x = self.__next(self.__x)
        return self.__normalize(self.__x)

