from format_output import (
    write_output_to_file, create_diagram, format_output_for_task3,
    get_trend, format_output_for_lab3
)
from services import (
    calculate_gravity_center, calculate_covariance,
    calculate_average_square_deviation, calculate_dispersion
)
from utils import open_file, get_sorted_y_and_x_lists_from_input_data


def get_task1_result(x_list: list[int], y_list: list[int], correlation: float) -> str:
    create_diagram(x_list, y_list)
    return get_trend(correlation)


def get_task2_result(x_list: list[float], y_list: list[float]) -> tuple[tuple[float, float], float]:
    gravity_center = calculate_gravity_center(x_list, y_list)
    return gravity_center, calculate_covariance(x_list, y_list, gravity_center)


def get_task3_result(covariance: float, x_list: list[float], x_average: float, y_average: float) -> str:
    dispersion = calculate_dispersion(x_list, x_average)
    first_coefficient = covariance / dispersion
    second_coefficient = y_average - first_coefficient * x_average
    return format_output_for_task3(first_coefficient, second_coefficient)


def get_task4_result(
        x_list: list[float], y_list: list[float],
        x_average: float, y_average: float, covariance: float
) -> float:
    average_square_deviation_x = calculate_average_square_deviation(x_list, x_average)
    average_square_deviation_y = calculate_average_square_deviation(y_list, y_average)
    return covariance / (average_square_deviation_x * average_square_deviation_y)


def main() -> None:
    file_name = input("Ведіть ім'я файлу: ")
    input_data = open_file(file_name)
    y_list, x_list = get_sorted_y_and_x_lists_from_input_data(input_data)

    gravity_center, covariance = get_task2_result(x_list, y_list)
    correlation = get_task4_result(x_list, y_list, gravity_center[0], gravity_center[1], covariance)
    trend_report = get_task1_result(x_list, y_list, correlation)
    equation = get_task3_result(covariance, x_list, gravity_center[0], gravity_center[1])

    output = format_output_for_lab3(trend_report, gravity_center, covariance, equation, correlation)
    write_output_to_file(output)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
