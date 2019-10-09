q = int(input())
for i in range(q):
    n = int(input())
    a = input().split(' ')
    allSum = 0
    for ai in a:
        allSum += int(ai)
    minPrice = allSum // n
    if n * minPrice < allSum:
        minPrice += 1
    print(minPrice)


