from typing import List


def find_average(numbers: List[int | float]) -> float:
    return sum(numbers) / len(numbers)


def gardners_equation(velocity: float) -> float:
    """Calculates the density based on the P-wave velocity. Ref. https://en.wikipedia.org/wiki/Gardner%27s_relation
    Args:
        velocity: float
    Returns:
        The density
    Raise:
        ValueError: In case a negative velocity is provided
    """
    if velocity < 0:
        raise ValueError

    alpha = 0.31
    beta = 0.25
    density = alpha * velocity**beta
    return density
