import matplotlib.pyplot as plt

utdanningsprogram = [
    "Bygg- og anleggsteknikk",
    "Elektro og datateknologi",
    "Helse- og oppvekstfag",
    "Naturbruk",
    "Restaurant- og matfag",
    "Teknologi- og industrifag",
    "Håndverk, design og produktutvikling",
    "Frisør, blomster, interiør og eksponeringsdesign",
    "Informasjonsteknologi og medieproduksjon",
    "Salg, service og reiseliv",
]

antall_gutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antall_jenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

fig, axs = plt.subplots(5, 2, constrained_layout=True)

axs = axs.flatten()

for ax, gutter, jenter, program in zip(
    axs, antall_gutter, antall_jenter, utdanningsprogram
):
    ax.pie((gutter, jenter), labels=("Gutter", "Jenter"))
    ax.set_title(program, fontsize=10)
plt.show()
