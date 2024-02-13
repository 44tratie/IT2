import json
import os


def last_inn_json(path: str, enc: str = "utf-8"):
    with open(path, encoding=enc) as json_file:
        data = json.load(json_file)
    return data


def data_er_gyldig(todos: list[dict], key_names: tuple[str, ...] = ()) -> bool:
    for todo in todos:
        if not all(key in todo for key in key_names):
            return False

    return True


def få_filbane(filnavn: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filnavn)
