def open_file(file_name: str) -> str:
    try:
        with open(f"src/data/{file_name}") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Напишіть дійсну назву файлу...")


def convert_list_items_to_type(type_, list_):
    return list(map(type_, list_))


def get_movie_views_from_input_data(input_data: str) -> list[int]:
    return convert_list_items_to_type(int, input_data.splitlines()[1:])


def get_sorted_dict(dict_: dict) -> dict:
    return dict(sorted(dict_.items(), key=lambda item: item[1]))
