with open("periode 1/Uke 42/computas/penger.txt", encoding="utf-8") as data_file:
    data = data_file.read()

from collections import Counter

print(sorted(Counter(data.split()).keys()))

prefiks_dict = {str(i): i for i in range(51)}
prefiks_dict_to = {
    "en": 1,
    "to": 2,
    "tre": 3,
    "fire": 4,
    "fem": 5,
    "seks": 6,
    "syv": 7,
    "åtte": 8,
    "ni": 9,
    "ti": 10,
}
prefiks_dict.update(prefiks_dict_to)

verdi_dict = {
    "kr": 1,
    "kroner": 1,
    "femkroner": 5,
    "femkrone": 5,
    "femmer": 5,
    "femmere": 5,
    "femtilapp": 50,
    "femtilapper": 50,
    "hundrelapp": 100,
    "hundrelapper": 100,
    "tier": 10,
    "tiere": 10,
    "tikrone": 10,
    "tikroner": 10,
    "tohundrelapp": 200,
    "tohundrelapper": 200,
}

summen = 0
for line in data.split("\n"):
    terms = line.split(", ")
    for term in terms:
        gevinst = term.split(" og ")
        # print(gevinst)
        for real in gevinst:
            prefiks, verdi = real.split()
            assert prefiks in prefiks_dict
            assert verdi in verdi_dict
            print(f"{prefiks} * {verdi} = {prefiks_dict[prefiks] * verdi_dict[verdi]}")
            summen += prefiks_dict[prefiks] * verdi_dict[verdi]

print(summen)
