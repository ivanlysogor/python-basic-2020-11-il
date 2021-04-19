import asyncio
import requests
import json

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import sessionmaker

DB_URL = "https://my-json-server.typicode.com/typicode/demo/db"

Base = declarative_base()


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    data = Column(String)
    create_date = Column(DateTime, server_default=func.now())
    post_comments = relationship("Comments")

    __mapper_args__ = {"eager_defaults": True}


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(ForeignKey("posts.id"))
    data = Column(String)


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:example@localhost/hw3",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    async with async_session() as session:
        data = json.loads(requests.get(DB_URL).text)
        async with session.begin():
            for post in data['posts']:
                session.add(Posts(id=post['id'], data=post['title']))
            for comment in data['comments']:
                session.add(Comments(id=comment['id'],
                                     data=comment['body'],
                                     post_id=comment['postId']))

        await session.commit()

        await session.close()

if __name__ == "__main__":
    asyncio.run(async_main())
