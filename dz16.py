def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds


# Ввод количества секунд
total_seconds = int(input("Введите количество секунд: "))
hours, minutes, seconds = convert_seconds(total_seconds)

print(f"{total_seconds} секунд = {hours} часов, {minutes} минут, {seconds} секунд.")


def convert_temperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 9 / 5) + 32
    reaumur = celsius * 4 / 5
    return kelvin, fahrenheit, reaumur


# Запрос у пользователя температуры в градусах Цельсия
celsius_temp = float(input("Введите температуру в градусах Цельсия: "))
kelvin, fahrenheit, reaumur = convert_temperature(celsius_temp)

# Вывод результата
print(f"{celsius_temp}°C = {kelvin:.2f} K, {fahrenheit:.2f} °F, {reaumur:.2f} °Re")
