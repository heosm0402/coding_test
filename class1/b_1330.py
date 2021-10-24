# https://www.acmicpc.net/problem/1330
import sys



if __name__ == "__main__":
    number_1, number_2 = map(int, sys.stdin.readline().rstrip().split())
    if number_1 > number_2:
        print('>')
    elif number_1 < number_2:
        print('<')
    else:
        print('==')
