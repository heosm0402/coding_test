# https://www.acmicpc.net/problem/1284
import sys


if __name__ == "__main__":
    address_list = []
    while True:
        num = sys.stdin.readline().rstrip()
        if num == '0':
            break
        address_list.append(num)

    area_list = [0 for i in range(len(address_list))]
    for idx, address in enumerate(address_list):
        for part in address:
            if part == '1':
                area_list[idx] += 3
            elif part == '0':
                area_list[idx] += 5
            else:
                area_list[idx] += 4

        area_list[idx] += 1
        print(area_list[idx])
