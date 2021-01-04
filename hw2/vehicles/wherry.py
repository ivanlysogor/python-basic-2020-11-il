from hw2.helpers import add_debug
from .boat import Boat
from .mixinengine import MixinEngine


class Wherry(MixinEngine, Boat):
    """
    A wherry object adds an engine to a boat
    """

    @add_debug
    def __init__(self, weight, capacity, number_of_passengers,
                 engine_number_of_cylinders, engine_type, engine_capacity,
                 fuel=0):
        self.init_engine(engine_number_of_cylinders=engine_number_of_cylinders,
                         engine_type=engine_type,
                         engine_capacity=engine_capacity, fuel=fuel)
        super().__init__(weight=weight, capacity=capacity,
                         number_of_passengers=number_of_passengers)

    @add_debug
    def __str__(self):
        return f"This is a wherry object with the following attributes:\n" \
               f"{{capacity : '{self.capacity}', " \
               f"weight : '{self.weight}', " \
               f"number_of_passengers : '{self._number_of_passengers}', " \
               f"engine : '{self._engine}'" \
               f"}}"

    @add_debug
    def make_beep(self):
        print(f'{self.__class__.__name__} Tuuuuuu-Tuuuuu')
