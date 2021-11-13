

import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    # N, K = 25, 3

    cnt = 0
    while N != 1:
        if N % K == 0:
            N /= K
        else:
            N -= 1
        cnt += 1
    
    print(cnt)