n = int(raw_input().strip())

X = [int(x) for x in raw_input().strip().split(' ')]
Y = [int(x) for x in raw_input().strip().split(' ')]

X.sort()
Y.sort()

numberOfOperations = 0
count = 0

for i in xrange(0, n):
    if X[i] != Y[i]:
        if X[i] < Y[i]:
            numberOfOperations += Y[i] - X[i]
            count += Y[i] - X[i]
            X[i] += Y[i] - X[i]
        else:
            numberOfOperations += X[i] - Y[i]
            count -= X[i] - Y[i]
            X[i] -= X[i] - Y[i]


if count == 0:
    print numberOfOperations / 2
else :
    print -1
