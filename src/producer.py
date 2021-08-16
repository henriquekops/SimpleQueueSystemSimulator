#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Producer:

    """
    Producer:
        - Generates a sequence of random numbers using linear congruent method
    Methods:
        - __init__()
        - generate(a, c, m)
    """

    def __init__(self, x) -> None:
        """
        Params:
            - x: starting seed for random sequence
        """
        self.__x = x
    
    def __next(self, x:int, a:int, c:int, m:int) -> int:
        """
        Params:
            - x: seed to consider
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
        Returns:
            - Next random value in sequence
        """
        return ((a * x) + c) % m

    def __generate(self, lst:List[int], x:int, a:int, c:int, m:int, i:int) -> List[int]:
        """
        @Overload

        Params:
            - lst: list to keep sequence
            - x: seed to consider
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
            - i: recursion iterator
        Returns:
            - Random integer sequence based on initial seed and params
        """
        if i == m:
            return lst
        else:
            i += 1
            x = self.__next(x, a, c, m)
            lst.append(x)
            return self.__generate(lst, x, a, c, m, i)


    def generate(self, a:int, c:int, m:int) -> List[int]:
        """
        Params:
            - a: sequence multiplier
            - c: constant for variation of sequence
            - m: max size of random value in sequence
        Returns:
            - Random integer sequence based on initial seed and params
        """
        i = 0
        x = self.__x
        lst = []
        return self.__generate(lst, x, a, c, m, i)


# Test #

if __name__ == '__main__':
    p = Producer(7)
    l = p.generate(4, 4, 9)
    print(l)
