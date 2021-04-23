from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from .database import db


class Flats(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True,
                  nullable=False, default="",
                  server_default="")
    address = Column(String, unique=False)
    electricity_t1 = Column(Integer, default=0)
    hot_water = Column(Integer, default=0)
    cold_water = Column(Integer, default=0)
