import httpx
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

TMDB_API = os.getenv('TMDB_API')

async def fetch_movie_data(movie_title: str) -> int | str:
    if not movie_title:
        return 'Ошибка! Введите название фильма.'
    else:
        url = f'https://api.themoviedb.org/3/search/movie?include_adult=false&language=ru-Ru&query={movie_title}'

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {TMDB_API}'
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                film_id = response.json()['results'][0]['id']
                return film_id
            except Exception as e:
                print(e)
                return 'Ошибка! Фильм не найден. Попробуйте проверить название и попробовать еще раз.'

async def main():
    movie_title = 'Я плюю на Ваши могилы'
    data = await fetch_movie_data(movie_title)
    print(data)

if __name__ == '__main__':
    asyncio.run(main())