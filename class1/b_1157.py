# https://www.acmicpc.net/problem/1157

import sys
from collections import Counter


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip().upper()
    most_letter = Counter(word).most_common(n=2)

    if len(most_letter) == 1:
        print(most_letter[0][0])
    elif most_letter[0][1] == most_letter[1][1]:
        print("?")
    else:
        print(most_letter[0][0])
