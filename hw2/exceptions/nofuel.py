class NoFuelException(Exception):
    """
    An exception raised while trying to start engine without fuel
    """

    def __init__(self, fuel, message="Vehicle doesn't have enough fuel"):
        f_message = f'{message}. Current fuel level - {fuel}'
        super().__init__(f_message)
