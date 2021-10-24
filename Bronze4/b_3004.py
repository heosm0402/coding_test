# https://www.acmicpc.net/problem/3004
import sys
import math


if __name__ == "__main__":
    count = int(sys.stdin.readline().rstrip())

    if count >= 2:
        print((math.ceil(count/2)+1) * (math.floor(count/2)+1))
    else:
        print(2)
