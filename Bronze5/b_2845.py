# https://www.acmicpc.net/problem/2845
import sys


if __name__ == "__main__":
    people, area = map(int, sys.stdin.readline().rstrip().split())
    people_news_list = list(map(int, sys.stdin.readline().rstrip().split()))

    diff = [people_news - (people * area) for people_news in people_news_list]

    print(*diff)
