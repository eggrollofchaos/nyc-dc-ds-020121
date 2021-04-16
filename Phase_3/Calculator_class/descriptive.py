#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""


class Calculator:
    def __init__(self, dataList):
        self.data = dataList
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_std()

    def __calc_mean(self):
        mean = sum(self.data)/self.length
        return mean

    def __calc_median(self):
        sorted_data = sorted(self.data)
        if self.length % 2: # odd number of elements
            median = sorted_data[self.length//2]
        else:
            median = (sorted_data[self.length//2 - 1] + sorted_data[self.length//2]) / 2
        return median

    def __calc_variance(self):
        variance = sum([(i - self.mean)**2 for i in self.data])/ (self.length - 1)
        return variance

    def __calc_std(self):
        std = (self.variance)**(0.5)
        return std

    def add_data(self, dataList):
        self.data.extend(dataList)
        self.length += len(dataList)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_std()

    def remove_data(self, dataList):
        self.data.remove(*dataList)
        self.length -= len(dataList)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.stand_dev = self.__calc_std()

    # pass
