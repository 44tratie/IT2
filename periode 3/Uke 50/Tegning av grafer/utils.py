from typing import Callable


def derivert(
    f: Callable[[float], float], delta_x: float = 1e-4
) -> Callable[[float], float]:
    def den_deriverte(x: float) -> float:
        return (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

    return den_deriverte
