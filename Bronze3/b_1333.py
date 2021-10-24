# https://www.acmicpc.net/problem/1333
import sys


if __name__ == "__main__":
    N, L, D = map(int, sys.stdin.readline().rstrip().split())

    song_playing = []
    for _ in range(N):
        song_playing.extend([0 for _ in range(L)])
        song_playing.extend([1 for _ in range(5)])

    while True:
        if song_playing[D] == 1:
            print(D)
            break
        else:
            if D < len(song_playing):
                D += D
                if D >= len(song_playing):
                    print(D)
                    break
            else:
                break
