from modeller.TodoApp import TodoApp
from verktøy import data_er_gyldig, få_filbane, last_inn_json


def main() -> None:
    json_data = last_inn_json(få_filbane("todos.json"))

    if not data_er_gyldig(json_data, ("userId", "id", "title", "completed")):
        print("Data er mangelfull, vennligst rens data (impl senere?)")
        exit(1)

    app = TodoApp.les_json(json_data)

    app.vis_todos()


if __name__ == "__main__":
    main()
