N, K, T = int(input().split())

fargetoner = list(map(input().split()))

fargetoner.sort()

par = 0

while len(fargetoner) > 1:
    sokk_1 = fargetoner.pop()
    sokk_2 = fargetoner.pop()

    if sokk_1 - sokk_2 <= T:
        par += 1
    else:
        fargetoner.append(sokk_2)

print(par)
