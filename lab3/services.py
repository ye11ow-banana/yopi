from functools import reduce
from math import sqrt


def calculate_mean(list_: list[float]) -> float:
    return reduce(lambda x, y: x + y, list_) / len(list_)


def calculate_gravity_center(x_list: list[float], y_list: list[float]) -> tuple[float, float]:
    return calculate_mean(x_list), calculate_mean(y_list)


def calculate_covariance(
        x_list: list[float], y_list: list[float], gravity_center: tuple[float, float]
) -> float:
    return sum(
        map(lambda _: _[0] * _[1], zip(x_list, y_list))
    ) / len(x_list) - gravity_center[0] * gravity_center[1]


def calculate_dispersion(list_: list[float], mean: float) -> float:
    return reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, list_)) / len(list_)


def calculate_average_square_deviation(list_: list[float], mean: float) -> float:
    return sqrt(calculate_dispersion(list_, mean))
