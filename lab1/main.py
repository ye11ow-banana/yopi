from format_output import (
    format_output_for_task1, format_output_for_task2, format_output_for_task3,
    write_output_to_file, create_task4_graph
)
from services import (
    get_frequencies, get_cumulative_frequencies, get_max_values, calculate_modes, calculate_median,
    calculate_dispersion, calculate_standard_deviation
)
from utils import open_file, get_movie_views_from_input_data, get_sorted_dict


def get_task1_result(movie_views: list[int]) -> str:
    frequencies = get_sorted_dict(get_frequencies(movie_views))
    cumulative_frequencies = get_cumulative_frequencies(frequencies)
    max_values = get_max_values(movie_views)
    return format_output_for_task1(frequencies, cumulative_frequencies, max_values)


def get_task2_result(movies_views: list[int]) -> str:
    modes = calculate_modes(movies_views)
    median = calculate_median(movies_views)
    return format_output_for_task2(modes, median)


def get_task3_result(movies_views: list[int]) -> str:
    dispersion = calculate_dispersion(movies_views)
    standard_deviation = calculate_standard_deviation(movies_views)
    return format_output_for_task3(dispersion, standard_deviation)


def get_task4_result(movies_views: list[int]) -> None:
    frequencies = get_sorted_dict(get_frequencies(movies_views))
    create_task4_graph(frequencies)


def main() -> None:
    file_name = input("Ведіть ім'я файлу: ")
    input_data = open_file(file_name)
    movie_views = get_movie_views_from_input_data(input_data)

    output = get_task1_result(movie_views)
    output += get_task2_result(movie_views)
    output += get_task3_result(movie_views)
    write_output_to_file(output)
    get_task4_result(movie_views)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
