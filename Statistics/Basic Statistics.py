# -*- coding: utf-8 -*-

"""
@author: Kley001
"""

#Here are some basic statistical functions that can be used from Python.

#Module and all the module libraries are imported:

import statistics
from statistics import *

#mean() is used to calculate the mean of a data set.
#Example:

data = [1, 2, 3]
mean = statistics.mean(data)
print(mean) 

#median() is used to calculate the median of a data set.
#Example:

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
median = statistics.median(data)
print(median)

#mode() is used to calculate the mode of a data set.
#Example:

data = [10, 20, 30, 40, 40, 40, 50, 60, 70, 80]
mode = statistics.mode(data)
print(mode) 

#variance() is used to calculate the variance of a data set.
#Example:

data = [2, 4, 6, 8, 10]
variance = statistics.variance(data)
print(variance)

#stdev() is used to calculate the standard deviation of a data set.
#Example:

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13]
stdev = statistics.stdev(data)
print(stdev) #As the result has many decimal places, it is recommended to round.
round(stdev, 2) #Result rounded to two decimal places.

#harmonic_mean() is used to calculate the harmonic mean of a data set.
#Example:

data = [4, 6, 8, 10]
harmonic_mean = statistics.harmonic_mean(data)
print(round(harmonic_mean,2)) #Here you can see that it can also be rounded directly in the print

#I hope these examples of basic functions of the module called 'statistics' are useful to be used when necessary.