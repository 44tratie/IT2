from matplotlib import pyplot as plt

t_sove = 7
t_gåing = 1
t_spising = 2
t_klasserommet = 8
t_gaming = 6

handlingstid = [t_sove, t_gåing, t_spising, t_klasserommet, t_gaming]

plt.pie(handlingstid, labels=("sovetid", "gåing", "spising", "klasserommet", "gaming"))
plt.show()
