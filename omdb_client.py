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


# async def main():
#         gg = OmdbClient()
#         var1 = await gg.search_movie(title = "Big")
#         pprint(var1)
# asyncio.run(main())

# gg = OmdbClient()
#         names = ['Big', 'Green book', 'Hangover']
#         #id_number = ['tt0089560', 'tt0499549']
#         list_name = [gg.search_movie(name) for name in names]
#         #id_list = [gg.get_movie(id_n) for id_n in id_number]
#         all_names = await asyncio.gather(*list_name)
#         #all_id = await asyncio.gather(*id_list)
#         print(all_names)
#         #pprint(all_id, sort_dicts=False)
# asyncio.run(main())









