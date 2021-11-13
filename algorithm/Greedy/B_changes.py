import sys


if __name__ == "__main__":
    money = int(sys.stdin.readline().rstrip())
    
    list_coin = [500, 100, 50, 10]
    count_coin = 0

    for coin in list_coin:
        count_coin += money // coin
        money %= coin
    
    print(count_coin)

