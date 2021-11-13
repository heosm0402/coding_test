import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    adventurer = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

    result = 0
    member = 0
    for i in adventurer:
        member += 1
        if member >= i:
            result += 1
            member = 0
    
    print(result)