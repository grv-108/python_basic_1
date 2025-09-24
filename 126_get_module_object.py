# 126. Get Module Object

# Write a Python program to get the actual module object for a given object.

from inspect import getmodule
from math import sqrt
import pandas as pd
import numpy as np

print(getmodule(sqrt))
print(getmodule(pd))
print(getmodule(np))