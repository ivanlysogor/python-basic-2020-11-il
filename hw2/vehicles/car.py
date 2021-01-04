from hw2.helpers import add_debug
from .carriage import Carriage
from .mixinengine import MixinEngine


class Car(MixinEngine, Carriage):
    """
    A car object adds engine to a carriage
    """

    @add_debug
    def __init__(self, weight, capacity, number_of_wheels,
                 engine_number_of_cylinders, engine_type, engine_capacity,
                 fuel=0):
        self.init_engine(engine_number_of_cylinders=engine_number_of_cylinders,
                         engine_type=engine_type,
                         engine_capacity=engine_capacity,
                         fuel=fuel)
        super().__init__(weight=weight, capacity=capacity,
                         number_of_wheels=number_of_wheels)

    @add_debug
    def __str__(self):
        return f"This is a car object with the following attributes:\n" \
               f"{{capacity : '{self.capacity}', " \
               f"weight : '{self.weight}', " \
               f"number_of_wheels : '{self._number_of_wheels}', " \
               f"engine : '{self._engine}'" \
               f"}}"

    @add_debug
    def make_beep(self):
        print(f'{self.__class__.__name__} Beeeeeep')
