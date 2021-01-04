class EngineNotStartedException(Exception):
    """
    An exception raised while trying to stop not running engine
    """

    def __init__(self,
                 message="Trying to stop engine but it's not started yet."):
        super().__init__(message)
