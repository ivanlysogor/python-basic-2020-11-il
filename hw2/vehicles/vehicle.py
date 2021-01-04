from abc import ABC, abstractmethod
from hw2.helpers import add_debug


class Vehicle(ABC):
    """
    An abstract class for any vehicle
    Has following attributes:
    :capacity
    :weight

    Shoud have following methods:
    :make_beep
    :start
    :stop
    """

    @add_debug
    def __init__(self, weight, capacity):
        self.weight = weight
        self.capacity = capacity

    @abstractmethod
    def make_beep(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @add_debug
    def capacity(self):
        return self._capacity

    @capacity.setter
    @add_debug
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    @add_debug
    def weight(self):
        return self._weight

    @weight.setter
    @add_debug
    def weight(self, weight):
        self._weight = weight
        return weight
