# https://www.acmicpc.net/problem/1333
import sys


if __name__ == "__main__":
    N, L, D = map(int, sys.stdin.readline().rstrip().split())

    song_playing = []
    for _ in range(N):
        song_playing.extend([0 for _ in range(L)])
        if _ != N - 1:
            song_playing.extend([1 for _ in range(5)])
    # print(song_playing)

    answer = 0
    while answer < len(song_playing):
        if song_playing[answer]:
            break
        answer += D
    print(answer)