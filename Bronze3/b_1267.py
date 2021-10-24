# https://www.acmicpc.net/problem/1267
import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    sec_list = list(map(int, sys.stdin.readline().rstrip().split()))

    total_y = 0
    total_m = 0
    for sec in sec_list:
        total_y += ((sec // 30) + 1) * 10
        total_m += ((sec // 60) + 1) * 15

    if total_m < total_y:
        print(f"M {total_m}")
    elif total_y < total_m:
        print(f"Y {total_y}")
    else:
        print(f"Y M {total_y}")
