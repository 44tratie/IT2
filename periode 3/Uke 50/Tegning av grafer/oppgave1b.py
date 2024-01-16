import numpy as np
from matplotlib import pyplot as plt

from utils import derivert


def f(x: float) -> float:
    return x**3


x = np.linspace(-2, 2, 100)

y_1 = f(x)
y_2 = derivert(f)(x)
y_3 = derivert(derivert(f))(x)

ys = (y_1, y_2, y_3)
titles = ["Grafen til $f" + "'" * i + "(x)$" for i in range(3)]
labels = ("$f(x) = x^3$", "$f'(x) = 3x^2$", "$f''(x) = 6x$")
colors = ("blue", "red", "green")

fig, axes = plt.subplots(3, 1, constrained_layout=True)

for y, color, label, title, ax in zip(ys, colors, labels, titles, axes):
    ax.plot(x, y, color=color, label=label)
    ax.set_title(title)
    ax.axhline(y=0, color="black", linestyle="dotted")
    ax.axvline(x=0, color="black", linestyle="dotted")
    ax.legend(loc="upper right")

# for i, ax in enumerate(axes):
#     ax.plot(x, y[i], color=colors[i], label=labels[i])
#     ax.set_title("Grafen til $f" + "'" * i + "(x)$")
#     ax.axhline(y=0, color="black", linestyle="dotted")
#     ax.axvline(x=0, color="black", linestyle="dotted")
#     ax.legend(loc="upper right")

fig.suptitle("Grafen til $f(x)$, $f'(x)$ og $f''(x)$")

plt.savefig("1b")
plt.show()
