from matplotlib import pyplot as plt

RESULTS_DIR_PATH = "src/results/"


def write_output_to_file(output: str) -> None:
    with open(f"{RESULTS_DIR_PATH}result.txt", "w", encoding="utf-8-sig") as file:
        file.write(output)


def create_diagram(min_: int, max_: int, q1: float, q2: float, q3: float) -> None:
    fig, ax = plt.subplots()
    boxes = [{"label": "Diagram", "whislo": min_, "q1": q1, "med": q2, "q3": q3, "whishi": max_}]
    ax.bxp(boxes, showfliers=False)
    plt.savefig(f"{RESULTS_DIR_PATH}result.jpg")


def create_table_for_stem_and_leaf_data(stem_and_leaf_data: dict[str, list[str]]) -> str:
    output = "Stem Leaf\n"
    for stem, leafs in stem_and_leaf_data.items():
        file_line = f" {stem} | "
        for leaf in leafs:
            file_line += f"{leaf} "
        output += f"{file_line}\n"
    return output


def format_output_for_lab2(
        q1: float, q3: float, p90: float, average_square_deviation: float,
        z_score: float, rearranged_list: list[float], stem_and_leaf_data: dict[str, list[str]]
) -> str:
    output = "Задача №1:\n"
    output += f"Q1 = {q1}\n"
    output += f"Q3 = {q3}\n"
    output += f"P90 = {p90}\n"
    output += "Задача №2:\n"
    output += f"Середнє квадратичне відхилення = {average_square_deviation}\n"
    output += f"Стандартне відхилення = {z_score}\n"
    output += f"Задача №3:\n"
    output += f"Відредаговані оцінки = {rearranged_list}\n"
    output += f"Задача №4:\n"
    output += f"Діаграма стовбур-листя\n"
    output += create_table_for_stem_and_leaf_data(stem_and_leaf_data)
    return output
