from typing import Self

from .Todo import Todo


class TodoApp:
    def __init__(self, data: list[Todo]) -> None:
        self.todos = data

    @classmethod
    def les_json(cls, json_data: list[dict]) -> Self:
        return cls([Todo(**todo) for todo in json_data])

    def legg_til_todo(self, todo: Todo) -> None:
        self.todos.append(todo)

    def vis_todos(self, sorter_etter: str = "id", synkende: bool = False) -> None:
        if sorter_etter not in Todo.model_fields:
            print(f"Kan ikke sortere etter {sorter_etter}")
            print(f"Gyldige sorteringsnøkler: {', '.join(Todo.model_fields)}")
            return

        for todo in sorted(
            self.todos, key=lambda todo: getattr(todo, sorter_etter), reverse=synkende
        ):
            print(todo)

    # def filtrer_():
    #     return filter(lambda todo: todo.completed)
