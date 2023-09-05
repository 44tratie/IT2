import random

n = 10

tall = [random.randint(1, 6) for _ in range(n)]

print(f"summen av tallene: {sum(tall)}")
print(f"gjennomsnittet av tallene: {sum(tall) / len(tall)}")
