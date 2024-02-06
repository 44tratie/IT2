import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos_oppgave2.json")

with open(path) as todos_file:
    data = json.load(todos_file)


def rens_data(data: list[dict]):
    renset_data = []
    ids = set()
    for todo in data:
        # tving datatyper
        todo["userId"] = int(todo["userId"])
        todo["id"] = int(todo["id"])

        # hopp over duplikate ider
        if todo["id"] in ids:
            continue

        # fjern ekstra space og newlines fra title
        todo["title"] = " ".join(todo["title"].split())

        # omgjør dager til int med defaultverdi 1
        todo["estimat"] = todo["estimat"][:-1]
        todo["estimat"] = int(todo["estimat"]) if todo["estimat"] else 1

        renset_data.append(todo)
        ids.add(todo["id"])

    return renset_data


data = rens_data(data)
print(data)
