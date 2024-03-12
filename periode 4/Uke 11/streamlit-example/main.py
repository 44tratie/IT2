import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

# Lager 2 glidere på applikasjonen,
# som returnerer gjeldende verdi her i koden
a = st.slider("a", min_value=-10, max_value=10)
b = st.slider("b", min_value=-10, max_value=10)
c = st.slider("c", min_value=-10, max_value=10)


# Lineær funksjon gitt ved: f(x) = ax + b
def f(x: float) -> float:
    return a * x**2 + b * x + c


x = np.linspace(-10, 10, 1000)

plt.plot(x, f(x))
plt.ylim(top=100, bottom=-100)
plt.grid()
plt.title(f"$f(x) = {a}x^2 + {b}x + {c}$")

st.write(plt.gcf())
