#!/bin/python
'''
	Thanks to https://github.com/segunfamisa for a wonderful explanation
	on this problem
'''
import sys

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

# if the number of sticks available is 1, we need to cut into 3 parts
if len(a) == 1:
    print 2
else:
	# we search for a stick whose length is greater than or equal to
	# the sum of the other sticks
	# if such a stick is found, this stick can be cut
    prefixSum = [0]

    for i in xrange(0, len(a)):
        prefixSum.append(prefixSum[i] + a[i])

    prefixSum.append(prefixSum[n])

    for i in xrange(0, len(a)):
        if a[i] >= prefixSum[i] + prefixSum[n + 1] - prefixSum[i + 1]:
            print 1
            break

        if i + 1 >= n:
            print 0
