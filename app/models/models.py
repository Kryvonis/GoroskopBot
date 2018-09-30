# -*- encoding: utf-8 -*-
import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app import db_engine
from app.settings import Config


Base = declarative_base()


class ZodiacEnum(enum.Enum):
    aries = 'aries'
    taurus = 'taurus'
    gemini = 'gemini'
    cancer = 'cancer'
    leo = 'leo'
    virgo = 'virgo'
    libra = 'libra'
    scorpio = 'scorpio'
    sagittarius = 'sagittarius'
    capricorn = 'capricorn'
    aquarius = 'aquarius'
    pisces = 'pisces'


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    is_bot = Column(Boolean)
    first_name = Column(String(250))
    last_name = Column(String(250))
    username = Column(String(250), nullable=True)
    language_code = Column(String(5))
    zodiac_sign = Column(Enum(ZodiacEnum), nullable=True)
    chats = Column(Integer)


if Config.CREATE_TABLES:
    res = Base.metadata.create_all(db_engine)

user = User.__table__