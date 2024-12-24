from urllib import response
import requests
from plyer import notification


# Просто сделаем запрос без функций

url = r"https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru"

response = requests.get(url)  # Сделали запрос и получили объект ответа
print(response.status_code)  # Получили статус ответа
print(response.json())  # Получили объект Python из JSON

# Получим описание и температуру, и ощущается как
weather_dict = response.json()

# Temp
temp = weather_dict["main"]["temp"]

# Ощущается как
feels_like = weather_dict["main"]["feels_like"]

# Описание погоды
description = weather_dict["weather"][0]["description"]

print(f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}")

# Уведомление
notification.notify(
    title="Погода в Череповце",
    message=f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}",
    app_name="Weather",
    app_icon=None,
)
