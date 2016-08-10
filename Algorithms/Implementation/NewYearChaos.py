#!/bin/python

import sys

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    # your code goes here
    numberOfBribes = 0
    numberOfBribesAnIndividualCanAfford = 2 #stated in question
    for i in xrange(len(q) - 1, 0, -1):
		# immediately you discover that the current state requires that
		# people be more corrupt than we originally assumed, we stop the process
        if numberOfBribes == -1:
            break

        # in as much as the the referenced individual was not bribed,
        # we continue searching for anybody that was bribed
        if q[i] > q[i-1]:
            continue
        else:
			indexOfCorruptIndividual = i-1
			for j in xrange(i - 1, i + 1):
				if j + 1 >= len(q):
					break
				if q[j] > q[j+1]:
					tmp = q[j]
					q[j] = q[j+1]
					q[j+1] = tmp
					numberOfBribes += 1
					indexOfCorruptIndividual = j + 1

			if indexOfCorruptIndividual + 1 >= len(q):
				continue
			elif q[indexOfCorruptIndividual] > q[indexOfCorruptIndividual + 1]:
				numberOfBribes = -1

    if numberOfBribes == -1 :
        print "Too chaotic"
    else:
        print numberOfBribes
