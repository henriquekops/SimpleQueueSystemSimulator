#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from matplotlib import pyplot as plt

class Display:

    @classmethod
    def plot(cls, sequence: List[int]) -> None:
        """
        - Plot chart of sequence

        - Parameters:
            - sequence: pseudo-random sequence of integers
            
            Return: None
        """
        plt.plot(list(range(0, len(sequence))), sequence, 'ro')
        plt.xlabel('sequence')
        plt.ylabel('quantity')
        plt.show()

