from sqlalchemy import MetaData, Table, Column, Integer, Numeric, String, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncio

meta = MetaData()

engine = create_async_engine("sqlite+aiosqlite:///mod.db", echo=False)

class Model:
    mod = Table('mod', meta,
            Column('id', Integer(), primary_key=True, autoincrement=True),
            Column('title', String(15), nullable=False),
            Column('year', String(5), nullable=False),
            Column('imdb_id', String(20), nullable=False),
            Column('poster', String(255), nullable=False),
            Column('user_rating', Integer())
            )

async def async_main() -> None:
     async with engine.begin() as conn:
         await conn.run_sync(meta.drop_all)
         await conn.run_sync(meta.create_all)

asyncio.run(async_main())

# for t in meta.tables:
#     print(meta.tables[t])


