from format_output import write_output_to_file
from format_output import create_diagram, format_output_for_lab2
from services import (
    calculate_q_or_p, calculate_average_square_deviation, calculate_standard_deviation,
    calculate_z_score, calculate_mean, get_rearranged_list_for_teacher, create_stem_and_leaf_data
)
from utils import open_file, get_sorted_scores_from_input_data


def get_task1_result(scores: list[int]) -> tuple[float, float, float]:
    q1 = calculate_q_or_p(scores, 0.25)
    q3 = calculate_q_or_p(scores, 0.75)
    p90 = calculate_q_or_p(scores, 90/100)
    return q1, q3, p90


def get_task2_result(scores: list[int], mean: float) -> tuple[float, float]:
    average_square_deviation = round(calculate_average_square_deviation(scores, mean), 2)
    standard_deviation = calculate_standard_deviation(scores, mean)
    z_score = round(calculate_z_score(scores[0], mean, standard_deviation), 2)
    return average_square_deviation, z_score


def get_task3_result(scores: list[int], mean: float) -> list[float]:
    return get_rearranged_list_for_teacher(scores, mean)


def get_task4_result(scores: list[int]) -> dict[str, list[str]]:
    return create_stem_and_leaf_data(scores)


def get_task5_result(scores: list[int], q1: float, q3: float) -> None:
    q2 = calculate_q_or_p(scores, 0.5)
    create_diagram(scores[0], scores[-1], q1, q2, q3)


def main() -> None:
    file_name = input("Ведіть ім'я файлу: ")
    input_data = open_file(file_name)
    scores = get_sorted_scores_from_input_data(input_data)

    mean = calculate_mean(scores)

    q1, q3, p90 = get_task1_result(scores)
    average_square_deviation, z_score = get_task2_result(scores, mean)
    rearranged_list = get_task3_result(scores, mean)
    stem_and_leaf_data = get_task4_result(scores)
    get_task5_result(scores, q1, q3)

    output = format_output_for_lab2(
        q1, q3, p90, average_square_deviation, z_score, rearranged_list, stem_and_leaf_data)
    write_output_to_file(output)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
