def open_file(file_name: str) -> str:
    try:
        with open(f"src/data/{file_name}") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Напишіть дійсну назву файлу...")


def convert_list_items_to_type(type_, list_):
    return list(map(type_, list_))


def get_sorted_scores_from_input_data(input_data: str) -> list[int]:
    return sorted(convert_list_items_to_type(int, input_data.splitlines()[1:]))
