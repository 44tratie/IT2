import random

arr = [random.randint(0, 100) for _ in range(50)]

arr.sort()


def join(sequence) -> str:
    return ", ".join(map(str, sequence))


print(f"alle partallene: {join(filter(lambda item: not item % 2, arr))}")
print(f"alle oddetallene: {join(filter(lambda item: item % 2, arr))}")
print(f"alle partallsindeks: {join((arr[i] for i in range(0, len(arr), 2)))}")
print(f"omvendt rekkefølge: {join(reversed(arr))}")
