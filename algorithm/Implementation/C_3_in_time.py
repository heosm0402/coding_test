import sys


# N = int(sys.stdin.readline().rstrip())
N = 5
result = (15*60) + (45*15)
for i in range(N):
    if i+1 == 3:
        result += 3600
    else:
        result += ((15*60) + (45*15))

print(result)
