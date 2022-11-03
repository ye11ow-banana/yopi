from typing import Iterable


def open_file(file_name: str) -> str:
    try:
        with open(f"src/data/{file_name}") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Напишіть дійсну назву файлу...")


def convert_list_items_to_type(type_, list_):
    return list(map(type_, list_))


def get_sorted_y_and_x_lists_from_input_data(input_data: str) -> Iterable[list]:
    y_and_x_list = zip(*map(lambda _: _.split("\t"), input_data.replace(',', '.').splitlines()[1:]))
    return map(lambda _: convert_list_items_to_type(float, _), y_and_x_list)
