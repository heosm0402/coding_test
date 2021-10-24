# https://www.acmicpc.net/problem/1271
import sys


if __name__ == "__main__":
    money, subject = map(int, sys.stdin.readline().rstrip().split())

    money_per_subject = money // subject
    left_money = money % subject

    print(money_per_subject)
    print(left_money)
