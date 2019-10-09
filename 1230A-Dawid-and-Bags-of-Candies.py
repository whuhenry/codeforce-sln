bags = input().split(' ')
candies = []
total = 0
for bag in bags:
    candies.append(int(bag))
    total += int(bag)

flag = False
for candy in candies:
    if candy == total - candy:
        flag = True
        break

if candies[0] + candies[1] == candies[2] + candies[3] or candies[0] + candies[2] == candies[1] + candies[3] or candies[0] + candies[3] == candies[1] + candies[2]:
    flag = True or flag
else:
    flag = False or flag

if flag:
    print('YES')
else:
    print('NO')

