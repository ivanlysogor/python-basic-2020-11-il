from hw2.helpers import add_debug
from .vehicle import Vehicle


class Boat(Vehicle):
    """
    A boat object adds property number_of_passengers to a vehicle
    """

    @add_debug
    def __init__(self, weight, capacity, number_of_passengers):
        self._number_of_passengers = number_of_passengers
        super().__init__(weight=weight, capacity=capacity)

    @add_debug
    def __str__(self):
        return f"This is a boat object with the following attributes:\n" \
               f"{{capacity : '{self.capacity}', " \
               f"weight : '{self.weight}', " \
               f"number_of_passengers : '{self._number_of_passengers}', " \
               f"}}"

    @add_debug
    def make_beep(self):
        print(f'{self.__class__.__name__} doesn\'t have a signal')

    @add_debug
    def start(self):
        print(f'{self.__class__.__name__} doesn\'t have an engine')

    @add_debug
    def stop(self):
        print(f'{self.__class__.__name__} doesn\'t have an engine')
