from datetime import datetime
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, validator, ValidationError
from hw2.helpers import add_debug


class EngineTypeEnum(str, Enum):
    diesel = 'diesel'
    gazoline = 'gazoline'


class Engine(BaseModel):
    """
    An engine data class
    Contains following attributes:
    :number_of_cylinders
    :engine_type - can be 'diesel' or 'gazoline'
    :engine_capacity
    """

    number_of_cylinders: int = 4
    engine_type: EngineTypeEnum = 'gazoline'
    engine_capacity: int = 1600

    @add_debug
    @validator('number_of_cylinders')
    def number_of_cylinders_validator(cls, v):
        if v < 0 or v > 12:
            raise ValueError('Incorrect number of cylinders')
        return v

    @add_debug
    @validator('engine_capacity')
    def engine_capacity_validator(cls, v):
        if v < 0:
            raise ValueError('Incorrect engine capacity')
        return v
