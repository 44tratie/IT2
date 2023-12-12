import random

import matplotlib.pyplot as plt

antall_kast = 100_000


def kast() -> int:
    return random.randint(1, 6)


x = (1, 2, 3, 4, 5, 6)
y = [0] * 6

for _ in range(antall_kast):
    y[kast() - 1] += 1

plt.plot(x, y)
plt.scatter(x, y)

plt.title(f"{antall_kast = }")
plt.xlabel("Antall øyne")
plt.ylabel("Antall utfall")

plt.savefig("2c")
plt.show()
