# 1, 1, 2, 3, 5, 8, 13

n = 4

tall = [1, 1]  # init

for _ in range(n - 2):
    tall.append(tall[-1] + tall[-2])

print(f"de {n} første fibonaccitallene er {', '.join(map(str, tall))}")
