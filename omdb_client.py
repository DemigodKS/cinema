import asyncio
import aiohttp
from pprint import pprint
class OmdbClient:
    async def search_movie(self, title: str) -> dict:
        url = "https://www.omdbapi.com/?apikey=fbdb7ba1"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params = {"t": title}) as response:
                data = await response.json()
        return data


    async def get_movie(self, imdb_id: str) -> dict:
        url = "https://www.omdbapi.com/?apikey=fbdb7ba1"
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params={"i": imdb_id, "plot":'full'}) as response:
                data1 = await response.json()
        return data1











