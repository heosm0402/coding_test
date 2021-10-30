# https://www.acmicpc.net/problem/2576
import sys

if __name__ == "__main__":
    numbers = []
    for _ in range(7):
        number = int(sys.stdin.readline().rstrip())
        if number % 2 == 1:
            numbers.append(number)

    if len(numbers) == 0:
        sys.stdout.write(str(-1) + '\n')
    else:
        sys.stdout.write(str(sum(numbers)) + '\n')
        sys.stdout.write(str(min(numbers)) + '\n')