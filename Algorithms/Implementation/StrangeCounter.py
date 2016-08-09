#!/bin/python

import sys

table1 = [3]
table2 = [1]
for i in xrange(0, 39):
    table1.append(table1[len(table1) - 1] * 2)
    table2.append(table1[len(table1) - 1] - 2)

t = int(raw_input().strip())

index = -1

for i in xrange(0, len(table2)) :
    if t == table2[i]:
        index = i
        break
    elif t < table2[i]:
        index = i - 1
        break

startHeightForInterval = table1[index]
startTimeForInterval = table2[index]

print startHeightForInterval - (t - startTimeForInterval)
