# https://www.acmicpc.net/problem/4388
import sys

if __name__ == "__main__":
    while True:
        n, m = sys.stdin.readline().rstrip().split()
        if int(n) + int(m) == 0:
            break

        min_len = min(len(n), len(m))
        cnt = 0
        for idx in range(min_len):
            idx_last = (idx + 1) * -1
            n_last, m_last = n[idx_last], m[idx_last]
            if int(n_last) + int(m_last) >= 10:
                cnt += 1

        if len(str(int(n) + int(m))) > len(str(max(int(n), int(m)))):
            cnt += 1

        print(cnt)
