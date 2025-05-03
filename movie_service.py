from sqlalchemy.orm.sync import update

from models import Model
import models
from omdb_client import OmdbClient
from models import engine
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

class Movie_service:
    async def add_movie_by_title(self, title: str):
        dd = OmdbClient()
        res = await dd.search_movie(title=title)
        print(res)
        async with engine.begin() as conn:
            await conn.execute(
                Model.mod.insert(), [{"title": res["Title"], "year": res["Year"], "imdb_id": res["imdbID"],
                                      "poster": res["Poster"]}])

    async def rate_movie(self, imdb_id: str, rating: int):
        dd = OmdbClient()
        res_ = await dd.get_movie(imdb_id=imdb_id)
        async with engine.begin() as conn:
            await conn.execute(
                Model.mod.update(), ({"user_rating": rating})
            )


async def main():
        ff = Movie_service()
        res1 = await ff.add_movie_by_title('Big')
        res2 = await ff.add_movie_by_title('Mask')

        res3 = await ff.rate_movie('tt0094737', 6)
        res4 = await ff.rate_movie('tt0089560', 8)

asyncio.run(main())


