#!/bin/python

import sys

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    count = 0
    for i in xrange(len(q) - 1, 0, -1):
        if count == -1:
            break
        if q[i] > q[i-1]:
            continue
        else:
            for j in xrange(i-1, i+1):
                if j + 1 >= len(q) :
                    break
                if q[j] > q[j+1]:
                    tmp = q[j]
                    q[j] = q[j+1]
                    q[j+1] = tmp
                    count += 1
            for j in xrange(i, i+2):
                if j + 1 >= len(q):
                    break
                if q[j] > q[j+1]:
                    count = -1

    if count == -1 :
        print "Too chaotic"
    else:
        print count


