from vehicles import Car
from vehicles import Wherry
from vehicles import Boat
from helpers import LOG_FILE


def main():

    print(f'Please check debug output at {LOG_FILE}\n')

    new_car = Car(capacity=500, weight=2000, number_of_wheels=4,
                  engine_number_of_cylinders=4, engine_type='gazoline',
                  engine_capacity=2000, fuel=5)
    print(new_car)
    new_car.make_beep()
    new_car.start()
    new_car.stop()

    print()
    new_boat = Boat(capacity=500, weight=2500,  number_of_passengers=2,)
    print(new_boat)
    new_boat.make_beep()
    new_boat.start()
    new_boat.stop()

    print()
    new_wherry = Wherry(capacity=50000, weight=60000, number_of_passengers=4,
                        engine_number_of_cylinders=12, engine_type='diesel',
                        engine_capacity=20000, fuel=50)
    print(new_wherry)
    new_wherry.make_beep()
    new_wherry.start()
    new_wherry.stop()
    print('Setting fuel to 0 and trying to start engine.')
    new_wherry.fuel = 0
    new_wherry.start()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Exception - {e.args}\n')
    finally:
        with open(LOG_FILE, 'r') as f:
            data = f.read()
            print(f'{data}')
