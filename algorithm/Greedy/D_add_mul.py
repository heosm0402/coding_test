import sys

if __name__ == "__main__":
    # S = sys.stdin.readline().rstrip()
    S = "02984"

    result = 0
    for i in S:
        num = int(i)
        if result <= 1 or num <= 1:
            result += num
        else:
            result *= num
    print(result)
