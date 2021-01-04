from hw2.exceptions import NoFuelException, \
                           AlreadyStartedException, EngineNotStartedException
from hw2.helpers import add_debug
from .engine import Engine


class MixinEngine():
    """
    A special class to add an engine to a vehicle

    Attributes:
    :fuel - amount of fuel

    Methods:
    :start - start engine
    :stop - stop engine
    """

    @add_debug
    def init_engine(self,
                    engine_number_of_cylinders,
                    engine_type, engine_capacity, fuel):
        self.fuel = fuel
        self._engine_started = False
        self._engine = Engine(number_of_cylinders=engine_number_of_cylinders,
                              engine_type=engine_type,
                              engine_capacity=engine_capacity)

    @add_debug
    def start(self):
        if self._fuel > 0:
            if not self._engine_started:
                print(f'{self.__class__.__name__} engine started')
                self._engine_started = True
            else:
                raise AlreadyStartedException()
        else:
            raise NoFuelException(self._fuel)

    @add_debug
    def stop(self):
        if self._engine_started:
            print(f'{self.__class__.__name__} engine stopped')
            self._engine_started = False
        else:
            raise EngineNotStartedException()

    @property
    @add_debug
    def fuel(self):
        return self._fuel

    @fuel.setter
    @add_debug
    def fuel(self, fuel):
        if fuel > 0:
            self._fuel = fuel
        else:
            raise NoFuelException(fuel)
