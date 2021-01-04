class AlreadyStartedException(Exception):
    """
    An exception raised while trying to start aleady
    started engine
    """

    def __init__(self,
                 message="Trying to start engine but it \
                 has been started already."):
        super().__init__(message)
