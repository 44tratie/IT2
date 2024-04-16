import cmd
import functools
import re
from typing import Callable, TypeVar

from backend.api import APIWrapper
from backend.api.omdb_models import BaseMedium
from backend.bucket_list import BucketList

T = TypeVar("T")


def type_confirm(types: list[Callable[[str], T]]):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(self, arguments: str):
            # arguments = re.findall(r"(\".+\"|.+)", arguments)
            arguments = re.findall(r"(\".+\"|\w+)", arguments)
            assert len(arguments) == len(types), "Invalid amount of arguments"

            try:
                arguments = [
                    type_(argument) for argument, type_ in zip(arguments, types)
                ]
                return f(self, *arguments)
            except ValueError:
                print("Invalid input")
                return

        return wrapper

    return decorator


class CLIApp(cmd.Cmd):
    prompt = ">>> "
    intro = "Welcome to Argsflix Bucket List CLI Application. Type 'help' for a list of commands."

    def __init__(self) -> None:
        super().__init__()
        self.api = APIWrapper()
        self.bucket_list = BucketList()

        self.list_key: dict[int, str] = {}
        self.current_search: dict[int, BaseMedium] = {}

    @type_confirm([str])
    def do_search(self, search_query: str) -> None:
        media = self.api.query_movie(search_query)

        for i, medium in enumerate(media, start=1):
            self.current_search[i] = medium
            print(f"{i}:\t{medium}\n")

    @type_confirm([int])
    def do_info(self, index: int) -> None:
        detailed_info = self.api.by_id(self.current_search[index].imdb_id)
        print(detailed_info)

    @type_confirm([int])
    def do_add(self, index: int) -> None:
        self.bucket_list.add_to_list(self.current_search[index])

    def do_list(self, _) -> None:
        for i, key in enumerate(self.bucket_list.list, start=1):
            print("SEEN" if key in self.bucket_list.seen else "NOT SEEN")

            self.list_key[i] = key
            print(f"{i}:\t{self.bucket_list.list[key]}\n")

    @type_confirm([int])
    def do_seen(self, index: int) -> None:
        self.bucket_list.update_seen(self.list_key[index])

    def do_reset(self, _) -> None:
        print("Resetted the bucket list")
        self.bucket_list.reset_list()

    def do_quit(self, _) -> None:
        return True


def main() -> None:
    app = CLIApp()
    app.cmdloop()


if __name__ == "__main__":
    main()
