from collections import Counter

import matplotlib.pyplot as plt

karakterer = [
    5,
    3,
    6,
    3,
    5,
    1,
    2,
    2,
    2,
    4,
    2,
    2,
    5,
    5,
    6,
    3,
    5,
    3,
    5,
    4,
    2,
    6,
    1,
    4,
    2,
    3,
    3,
    3,
    5,
    5,
]

counter = Counter(karakterer)
karakter_antall = [counter[i] for i in range(1, 7)]

plt.pie(karakter_antall, labels=[str(i) for i in range(1, 7)])

plt.show()
