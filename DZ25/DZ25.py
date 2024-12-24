# Импортируем full_dict из файла Marvel.py
from marvel import full_dict
from pprint import pprint

# 1. Реализуем ввод от пользователя
user_input = input("Введите ID фильмов через пробел: ")
id_list = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

# 2. Используем filter для создания словаря с фильмами по введенным ID
filtered_movies = {
    k: v for k, v in full_dict.items() if v["id"] in filter(None, id_list)
}

# 3. Создаем множество уникальных значений ключа 'director'
unique_directors = {movie["director"] for movie in full_dict.values()}

# 4. Создаем копию словаря, преобразуя каждое значение 'year' в строку
year_as_string_dict = {k: {**v, "year": str(v["year"])} for k, v in full_dict.items()}

# 5. Получаем словарь фильмов, начинающихся на букву 'Ч'
movies_starting_with_ch = {
    k: v for k, v in full_dict.items() if v["title"].startswith("Ч")
}

# 6. Сортируем словарь по одному параметру (например, по 'year')
sorted_by_year = dict(sorted(full_dict.items(), key=lambda item: item[1]["year"]))

# 7. Сортируем словарь по двум параметрам (например, по 'year' и 'title')
sorted_by_year_and_title = dict(
    sorted(full_dict.items(), key=lambda item: (item[1]["year"], item[1]["title"]))
)

# 8. **Опционально:** Фильтруем и сортируем в одном выражении
filtered_and_sorted = dict(
    sorted(
        filter(lambda item: item[1]["title"].startswith("Ч"), full_dict.items()),
        key=lambda item: item[1]["year"],
    )
)


# 9. **Опционально:** Добавляем аннотацию типов
def process_movies(full_dict: dict) -> None:
    # (весь код выше здесь)
    pass


# 10. Выводим результаты с помощью pprint
print("Фильтры по ID:")
pprint(filtered_movies)

print("\nУникальные режиссеры:")
pprint(unique_directors)

print("\nКопия словаря с годами в строковом формате:")
pprint(year_as_string_dict)

print("\nФильмы, начинающиеся на 'Ч':")
pprint(movies_starting_with_ch)

print("\nСортировка по году:")
pprint(sorted_by_year)

print("\nСортировка по году и названию:")
pprint(sorted_by_year_and_title)

print("\nФильтры и сортировка в одном выражении:")
pprint(filtered_and_sorted)
