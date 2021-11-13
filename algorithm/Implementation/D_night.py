import sys

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
point = sys.stdin.readline()

x, y = l.index(point[0]) + 1, int(point[1])
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

result = 0
for step in steps:
    if ((x + step[0]) >= 1) and ((y + step[1]) >=1):
        result += 1

print(result) 


