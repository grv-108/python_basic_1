# 125. Sum Collection Counts

# Write a Python program to sum all counts in a collection.

import collections

a = [x for x in range(10)]

print(sum(collections.Counter(a).values()))