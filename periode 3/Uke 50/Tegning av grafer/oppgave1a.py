import numpy as np
from matplotlib import pyplot as plt

from utils import derivert


def f(x: float) -> float:
    return x**3


x = np.linspace(-2, 2, 100)

y_1 = f(x)
y_2 = derivert(f)(x)
y_3 = derivert(derivert(f))(x)

plt.plot(x, y_1, color="blue")
plt.plot(x, y_2, color="red")
plt.plot(x, y_3, color="green")

plt.legend(["$f(x) = x^3$", "$f'(x) = 3x^2$", "$f''(x) = 6x$"])
plt.title("Grafen til $f(x)$, $f'(x)$ og $f''(x)$")

plt.axhline(y=0, color="black", linestyle="dotted")
plt.axvline(x=0, color="black", linestyle="dotted")

plt.savefig("1a")
plt.show()
