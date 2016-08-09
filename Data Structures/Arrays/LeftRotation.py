# Enter your code here. Read input from STDIN. Print output to STDOUT
line = [int(x) for x in raw_input().strip().split(' ')]
n = line[0]
d = line[1]

arr = [int(x) for x in raw_input().strip().split(' ')]

ans = [0] * len(arr)

for i in xrange(0, len(arr)):
    if i - d < 0:
        ans[len(arr) + (i - d)] = arr[i]
    else:
        ans[i - d] = arr[i]

print ' '.join([str(x) for x in ans])
