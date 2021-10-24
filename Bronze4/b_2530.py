# https://www.acmicpc.net/problem/2530
import sys
from datetime import datetime, timedelta


if __name__ == "__main__":
    h, m, s = map(int, sys.stdin.readline().rstrip().split())
    processing_time = int(sys.stdin.readline().rstrip())

    finish_time = datetime.now().replace(hour=h, minute=m, second=s, microsecond=0) \
                  + timedelta(seconds=processing_time)

    print(finish_time.hour, finish_time.minute, finish_time.second)
