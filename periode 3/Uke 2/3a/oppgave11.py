import matplotlib.pyplot as plt
import numpy as np

årstall = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]

antall_ap = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
antall_høyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

x_pos = np.arange(len(årstall))
plt.bar(x_pos - 0.2, antall_ap, width=0.4, label="AP", color="orange")
plt.bar(x_pos + 0.2, antall_høyre, width=0.4, label="Høyre", color="blue")
ax = plt.gca()
ax.set_xticks(x_pos, årstall)
ax.legend()
plt.show()
