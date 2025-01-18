import asyncio
import aiohttp
import markdown
from hw_27_data import DATA  # Импортируем данные из нового файла

API_URL = "https://api.vsegpt.ru/v1"  # Замените на актуальный URL API
API_KEY = "Ваш API ключ"  # Ваш API ключ
MAX_CHUNK_SIZE = 2000
SLEEP_TIME = 1


async def fetch_response(session, text):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini-turbo",  # Укажите модель, которую хотите использовать
        "messages": [{"role": "user", "content": text}],
        "max_tokens": 100,  # Настройте по необходимости
    }

    async with session.post(API_URL, json=payload, headers=headers) as response:
        return await response.json()


async def get_ai_request(session, texts):
    tasks = [fetch_response(session, text) for text in texts]
    responses = await asyncio.gather(*tasks)
    return responses


def split_text(text):
    return [text[i : i + MAX_CHUNK_SIZE] for i in range(0, len(text), MAX_CHUNK_SIZE)]


async def main():
    async with aiohttp.ClientSession() as session:
        all_responses = []
        for text in DATA:
            chunks = split_text(text)
            for chunk in chunks:
                response = await get_ai_request(session, [chunk])
                all_responses.append(response)
                await asyncio.sleep(SLEEP_TIME)  # Задержка между запросами

        # Обработка и сохранение результатов в формате Markdown
        with open("output.md", "w", encoding="utf-8") as f:
            for i, response in enumerate(all_responses):
                f.write(f"## Запрос {i + 1}\n")
                f.write(f"**Входные данные:** {DATA[i]}\n")
                f.write(
                    f"**Ответ API:** {response[0]['choices'][0]['message']['content']}\n\n"
                )
                f.write("---\n")


if __name__ == "__main__":
    asyncio.run(main())
