from functools import reduce
from math import sqrt


def get_frequencies(list_: list[int]) -> dict[int, int]:
    return {value: list_.count(value) for value in list_}


def get_cumulative_frequencies(frequencies: dict[int, int]) -> dict[int, int]:
    cumulative_frequencies = {}
    previous = 0
    for key, frequency in frequencies.items():
        cumulative_frequencies[key] = previous = frequency + previous
    return cumulative_frequencies


def get_max_values(list_: list[int]) -> list[tuple[int, int]]:
    max_value = max(list_)
    return [(index, value) for index, value in enumerate(list_, 1) if value == max_value]


def calculate_modes(list_: list[int]) -> list[int]:
    frequencies = get_frequencies(list_)
    max_value = max(frequencies.values())
    return [value for value, frequency in frequencies.items() if frequency == max_value]


def calculate_median(list_: list[int]) -> float:
    list_ = sorted(list_)
    half_length = len(list_) / 2
    return (list_[int(half_length - 0.5)] + list_[int(half_length)]) / 2


def calculate_mean(list_: list[int]) -> float:
    movies_views_length = len(list_)
    return reduce(lambda x, y: x + y, list_) / movies_views_length


def _calculate_numerator_dispersion(list_: list[int]) -> float:
    mean = calculate_mean(list_)
    result = 0
    for movie_views in list_:
        result += (movie_views - mean) ** 2
    return result


def calculate_dispersion(list_: list[int]) -> float:
    numerator = _calculate_numerator_dispersion(list_)
    return numerator / (len(list_) - 1)


def calculate_standard_deviation(list_: list[int]) -> float:
    numerator = _calculate_numerator_dispersion(list_)
    return sqrt(numerator / len(list_))
