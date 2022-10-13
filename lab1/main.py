from functools import reduce
from math import sqrt
from typing import TextIO

from matplotlib import pyplot as plt


def task1(movies_views: list[int], file: TextIO) -> None:
    row_format = "{:>3} {:>10}"
    file.write("Таблиця частот:\n")
    file.write("Фільм   Перегляди\n")
    for index, movie_views in enumerate(movies_views, 1):
        file.write(f"{row_format.format(index, movie_views)}\n")
    file.write("------------------\n")

    checked_movies = []
    file.write("Таблиця сукупних частот:\n")
    file.write("Частота   Перегляди\n")
    for movie_views in movies_views:
        if movie_views in checked_movies:
            continue
        frequency = movies_views.count(movie_views)
        checked_movies.append(movie_views)
        file.write(f"{row_format.format(frequency, movie_views)}\n")
    file.write("------------------\n")

    max_views = max(movies_views)
    for index, movie_views in enumerate(movies_views, 1):
        if max_views == movie_views:
            file.write(f"Фільм, переглянутий найчастіше: {index} -- {max_views}\n")


def task2(movies_views: list[int], file: TextIO) -> None:
    file.write(f"Мода: {max(movies_views)}\n")

    movies_views = sorted(movies_views)
    half_length = len(movies_views) / 2
    file.write(f"Медіана: {(movies_views[int(half_length - 0.5)] + movies_views[int(half_length)]) / 2}\n")


def task3(movies_views: list[int], file: TextIO) -> None:
    movies_views_length = len(movies_views)
    mean = reduce(lambda x, y: x + y, movies_views) / movies_views_length
    result = 0
    for movie_views in movies_views:
        result += (movie_views - mean) ** 2
    file.write(f"Дисперсія: {result / (movies_views_length - 1)}\n")

    file.write(f"Середнє квадратичне відхилення розподілу: {sqrt(result / movies_views_length)}\n")


def task4(movies_views: list[int]) -> None:
    plt.figure(figsize=(15, 6), dpi=80)
    plt.xlabel("Movies")
    plt.ylabel("Views")
    plt.bar([f"{_ * ' '}" for _ in range(len(movies_views))], movies_views)
    plt.savefig("result.jpg")


def main() -> None:
    file_name = input("Enter file name: ")
    try:
        with open(file_name) as file:
            movies_views = list(map(int, file.read().splitlines()[1:]))
    except FileNotFoundError:
        print("Напишіть дійсну назву файлу...")
        return

    with open("result.txt", "w", encoding="utf-8-sig") as file:
        file.write("Завдання №1:\n")
        task1(movies_views, file)

        file.write("Завдання №2:\n")
        task2(movies_views, file)

        file.write("Завдання №3:\n")
        task3(movies_views, file)

        task4(movies_views)


if __name__ == "__main__":
    main()
