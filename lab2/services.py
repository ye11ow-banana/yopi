from functools import reduce
from math import sqrt

import numpy as np

from utils import convert_list_items_to_type


def calculate_q_or_p(list_: list[int], fraction: float) -> float:
    index = int(fraction * (len(list_) + 1)) - 1
    return list_[index] + fraction * (list_[index + 1] - list_[index])


def calculate_mean(list_: list[int]) -> float:
    return reduce(lambda x, y: x + y, list_) / len(list_)


def _calculate_numerator_dispersion(list_: list[int], mean: float) -> float:
    list_ = map(lambda x: (x - mean) ** 2, list_)
    return reduce(lambda x, y: x + y, list_)


def calculate_average_square_deviation(list_: list[int], mean: float) -> float:
    numerator = _calculate_numerator_dispersion(list_, mean)
    return sqrt(numerator / (len(list_) - 1))


def calculate_standard_deviation(list_: list[int], mean: float) -> float:
    numerator = _calculate_numerator_dispersion(list_, mean)
    return sqrt(numerator / len(list_))


def calculate_z_score(integer: int, mean: float, standard_deviation: float) -> float:
    return (integer - mean) / standard_deviation


def _get_a_and_b(mean: float, to: int) -> np.ndarray:
    coefficients = [[100, 1], [mean, 1]]
    answers = [100, to]
    return np.linalg.solve(coefficients, answers)


def get_rearranged_list_for_teacher(list_: list[int], mean: float) -> list[float]:
    a, b = _get_a_and_b(mean, 95)
    return [round(value * a + b, 2) for value in list_]


def create_stem_and_leaf_data(list_: list[int]) -> dict[str, list[str]]:
    stem_and_leaf_data = {str(k): [] for k in range(10)}
    for value in convert_list_items_to_type(str, list_):
        stem, leaf = value[0], value[1:]
        if len(value) == 1:
            stem, leaf = "0", value
        stem_and_leaf_data[stem].append(leaf)
    return stem_and_leaf_data
