import numpy as np
from matplotlib import pyplot as plt

RESULTS_DIR_PATH = "src/results/"


def write_output_to_file(output: str) -> None:
    with open(f"{RESULTS_DIR_PATH}result.txt", "w", encoding="utf-8-sig") as file:
        file.write(output)


def create_diagram(x_axis: list[float], y_axis: list[float]) -> None:
    plt.scatter(x_axis, y_axis)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xticks(np.arange(min(x_axis), max(x_axis), 4))
    plt.yticks(np.arange(min(y_axis), max(y_axis), 0.5))
    plt.grid()
    plt.savefig(f"{RESULTS_DIR_PATH}result.jpg")


def format_output_for_task3(first_coefficient: float, second_coefficient: float) -> str:
    return f"y = {round(first_coefficient, 2)}x + {round(second_coefficient, 2)}"


def get_trend(correlation: float) -> str:
    if correlation > 0:
        return "Тренд позитивний"
    elif correlation < 0:
        return "Тренд негативний"
    else:
        return "Тренду не існує"


def format_output_for_lab3(
        trend_report: str, gravity_center: tuple[float, float],
        covariance: float, equation: str, correlation: float
) -> str:
    output = "Задача №1:\n"
    output += f"{trend_report}\n"
    output += "Задача №2:\n"
    output += f"Центр ваги = {tuple(map(lambda x: round(x, 2), gravity_center))}\n"
    output += f"Коваріація = {round(covariance, 2)}\n"
    output += f"Задача №3:\n"
    output += f"Рівняння лінії регресії: {equation}\n"
    output += f"Задача №4:\n"
    output += f"Коефіцієнт кореляції = {round(correlation, 2)}\n"
    return output
