# https://www.acmicpc.net/problem/2721
import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        number = int(sys.stdin.readline().rstrip())
        answer = 0
        for i in range(number):
            answer += (i+1) * sum([j+1 for j in range(i+2)])
        
        print(answer)