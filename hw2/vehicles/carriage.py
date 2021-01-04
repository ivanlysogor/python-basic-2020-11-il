from hw2.helpers import add_debug
from .vehicle import Vehicle


class Carriage(Vehicle):
    """
    A carriage object adds property number_of_wheels to a vehicle
    """

    @add_debug
    def __init__(self, weight, capacity, number_of_wheels=4):
        self._number_of_wheels = number_of_wheels
        super().__init__(weight=weight, capacity=capacity)

    @add_debug
    def make_beep(self):
        print(f'{self.__class__.__name__} doesn''t have a beep')

    @add_debug
    def start(self):
        pass

    @add_debug
    def stop(self):
        pass
