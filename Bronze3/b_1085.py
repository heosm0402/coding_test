# https://www.acmicpc.net/problem/1085
import sys
import math

if __name__ == "__main__":
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
    print(min(x, y, h-y, w-x))
