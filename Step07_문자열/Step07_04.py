t = int(input())
for i in range(1, t+1):
    repeat, s = input().split()
    for x in s:
        result = x * int(repeat)
        print(result, end = '')
    print()
    