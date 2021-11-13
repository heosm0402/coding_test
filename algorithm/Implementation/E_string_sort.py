import sys

S = sys.stdin.readline()

num = 0
list_alpha = ""
num_added = False
for i in S:
    if i.isdigit():
        num_added = True
        num += int(i)
    else:
        list_alpha += i

result = ''.join(sorted(list_alpha))

if num_added:
    result += str(num)

print(result)