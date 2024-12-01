import random
from cities import cities_list

def play_game(cities):
    used_cities = set()
    player_turn = True  # Ход игрока
    current_letter = ''  # Последняя буква города

    while True:
        if player_turn:
            player_city = input("Ваш ход! Назовите город или введите 'стоп' для выхода: ").strip()

            if player_city.lower() == 'стоп':
                print("Вы проиграли! Компьютер победил.")
                break

            # Проверка, существует ли город и не использовался ли он ранее
            if player_city not in cities or player_city in used_cities:
                print("Этот город недоступен или вы его уже назвали. Вы проиграли!")
                break

            # Удаляем город из доступных
            used_cities.add(player_city)
            current_letter = player_city[-1]  # Обновляем последнюю букву

        else:
            # Ход компьютера
            computer_city = next((city for city in cities if city[0] == current_letter and city not in used_cities), None)

            if computer_city:
                print(f"Компьютер назвал город: {computer_city}")
                used_cities.add(computer_city)
                current_letter = computer_city[-1]  # Обновляем последнюю букву
            else:
                print("Компьютер не может назвать город. Вы выиграли!")
                break

        player_turn = not player_turn  # Меняем очередь ходов

if __name__ == '__main__':
    play_game(cities_list)  # Начинаем игру с использованием списка городов

