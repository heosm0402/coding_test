# https://www.acmicpc.net/problem/1546
import sys


def calc_new_score(score):
    return score / max_score * 100


if __name__ == "__main__":
    subject_num = int(sys.stdin.readline().rstrip())
    subject_scores = list(map(int, sys.stdin.readline().rstrip().split()))

    max_score = max(subject_scores)

    new_scores = list(map(calc_new_score, subject_scores))
    print(sum(new_scores)/len(new_scores))
