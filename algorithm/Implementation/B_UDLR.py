import sys

# Right, Left, Down, Up
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(sys.stdin.readline().rstrip())
schedules = list(sys.stdin.readline().rstrip().split())

x, y = 1, 1
for schedule in schedules:
    if (schedule == "R"):
        if y <= (N-1):
            y += dy[0]
    if schedule == "L":
        if y >= 2:
            y += dy[1]
    if schedule == "U":
        if x >= 2:
            x += dx[3]
    if schedule == "D":
        if x <= (N-1):
            x += dx[2]


print(x, y)