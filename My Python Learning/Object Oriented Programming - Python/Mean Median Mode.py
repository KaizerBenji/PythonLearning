# Using Numpy to find mean median and mode

import numpy # Numerical Python package used while working with arrays
from scipy import stats # SciPy package 

nums = [45, 65, 23, 35, 65, 54, 34, 24, 27, 12, 1, 4, 7, 100]

mean_nums = numpy.mean(nums)
print(mean_nums)

median_nums = numpy.median(nums)
print(median_nums)

nums_mode = stats.mode(nums)
print(nums_mode)
