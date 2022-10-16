from matplotlib import pyplot as plt

from utils import convert_list_items_to_type

RESULTS_DIR_PATH = "src/results/"


def write_output_to_file(output: str) -> None:
    with open(f"{RESULTS_DIR_PATH}result.txt", "w", encoding="utf-8-sig") as file:
        file.write(output)


def create_table_of_frequencies(frequencies: dict[int, int], *, name: str, titles: str) -> str:
    table = name + "\n"
    table += titles + "\n"
    for views, frequency in frequencies.items():
        table += "{:>5} {:>10}".format(views, frequency, frequency) + "\n"
    return table


def format_output_for_max_values(max_values: list[tuple[int, int]]) -> str:
    output = ""
    for index, max_value in max_values:
        output += f"Фільм, переглянутий найчастіше: {index} -- {max_value}\n"
    return output


def format_output_for_task1(
        frequencies: dict[int, int], cumulative_frequencies: dict[int, int],
        max_values: list[tuple[int, int]]) -> str:
    output = "Завдання №1:\n"
    output += create_table_of_frequencies(frequencies, name="Таблиця частот:", titles="Перегляди   Частота")
    output += create_table_of_frequencies(
        cumulative_frequencies, name="Таблиця сукупних частот:", titles="Перегляди   Сукупна частота")
    output += format_output_for_max_values(max_values)
    return output


def format_output_for_modes(modes: list[int]) -> str:
    output = ""
    for views in modes:
        output += f"Мода: {views}\n"
    return output


def format_output_for_task2(modes: list[int], median: float) -> str:
    output = "Завдання №2:\n"
    output += format_output_for_modes(modes)
    output += f"Медіана: {median}\n"
    return output


def format_output_for_task3(dispersion: float, standard_deviation: float) -> str:
    output = "Завдання №3:\n"
    output += f"Дисперсія: {round(dispersion, 2)}\n"
    output += f"Середнє квадратичне відхилення розподілу: {round(standard_deviation, 2)}\n"
    return output


def create_size() -> None:
    plt.figure(figsize=(20, 8), dpi=80)


def name_labels(x_label: str, y_label: str) -> None:
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def generate_axes(dict_: dict[int, int]) -> None:
    y_axis = convert_list_items_to_type(str, dict_.keys())
    x_axis = dict_.values()
    plt.bar(y_axis, x_axis)


def save_graph_to_file(file_name: str) -> None:
    plt.savefig(file_name)


def create_task4_graph(frequencies: dict[int, int]) -> None:
    create_size()
    name_labels("Views", "Frequency")
    generate_axes(frequencies)
    save_graph_to_file(f"{RESULTS_DIR_PATH}result.jpg")
