#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class Display:

    @classmethod
    def plot_chart(cls, data) -> None:
        """
            Display data plot

            Parameters:
                data
            
            Return: None
        """
        plot_done = cls._build_plot()
        #plot_done.show()
        pass

    @classmethod
    def _build_plot(cls, data) -> plt:
        """
            Build and set plot charts

            Parameters:
                data
            
            Return: ploty object
        """
        pass
