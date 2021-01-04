import time
import operator
from functools import wraps
import pprint

EVEN = 1
ODD = 2
PRIME = 3


def list_powers(numbers, power=2):
    """
    Powers a list of numbers
    :param numbers: a list of number to power
    :param power: expected power (default is 2)
    :return: the new list of numbers
    """
    return list(map(operator.pow, numbers, [power] * len(numbers)))


def is_prime(x):
    """
    Checks if number is a prime
    :param x: A number to check
    :return: True|False
    """
    if x < 4:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x // 2, 2):
        if x % i == 0:
            return False
    return True


def is_even(x):
    """
    Checks if number is even
    :param x: A number to check
    :return: True|False
    """
    if x % 2 == 0:
        return True
    return False


def is_odd(x):
    """
    Checks if number is odd
    :param x: A number to check
    :return: True|False
    """
    if x % 2 != 0:
        return True
    return False


def time_estimation(func):
    """
    Decorator to add function execution time
    :param func: A func to decorate
    :return: A func result
    """
    @wraps(func)
    def estimation(*argc, **kargc):
        start_time = time.time()
        result = func(*argc, **kargc)
        delta_time = time.time()-start_time
        print(f'Function {func.__name__} execution time is {delta_time:.10f}')
        return result
    return estimation


@time_estimation
def select_numbers(numbers, number_type=EVEN):
    """
    Select en ODD, EVEN or SIMPLE numbers from a list
    :param numbers:  a list of numbers
    :param number_type: type of numbers to select (default = EVEN)
    :return: a filtered list
    """
    return list(filter({
                           number_type == EVEN: is_even,
                           number_type == ODD: is_odd,
                           number_type == PRIME: is_prime,
                        }[True], numbers))


def trace(func):
    """
    Decorator to show fibo nested level
    :param func: A func to decorate
    :return: A func result
    """
    @wraps(func)
    def wrapper(*argc, **kargc):
        print(f"{'-----' * (len(argc[0]) - 2)}--->{func.__name__}"
              f"({len(argc[0]) - 2})")
        res = func(*argc, **kargc)
        print(f"<---{'-----' * (len(argc[0]) - 2)}{func.__name__}"
              f"({len(argc[0]) - 2})")
        return res
    return wrapper


def fib(upto):
    """
    Calculated fibo list of numbers less then upto
    :param upto: a max number to calculate
    (calculate all fibo numbers less than upto)
    :return: a fibo list
    """
    @trace
    def fib_loop(fib_list, upto):
        if fib_list[-1] + fib_list[-2] < upto:
            return fib_loop(fib_list + [fib_list[-1] + fib_list[-2]], upto)
        else:
            return fib_list
    if upto < 1:
        return []
    if upto < 2:
        return [1]
    return fib_loop([1, 2], upto)


def comment(func, comment):
    @wraps(func)
    def wrapper(*argc, **kargc):
        print(f'{comment} with following argc {argc}')
        res = func(*argc, **kargc)
        pprint.pprint(res)
        print()
        return res
    return wrapper


if __name__ == "__main__":

    c_list_powers = comment(list_powers,
                            "Executing function list power")
    c_list_powers([1, 2, 3, 4, 5], 2)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    c_select_numbers = comment(select_numbers,
                               "Execuring function select numbers")
    c_select_numbers(numbers, PRIME)
    c_select_numbers(numbers, EVEN)
    c_select_numbers(numbers, ODD)

    c_fib = comment(fib,
                    'Executing function fib to get Fibonacchi numbers')
    c_fib(50)
