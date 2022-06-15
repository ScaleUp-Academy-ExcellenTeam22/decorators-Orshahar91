def surprise(_function):
    """
    Decorator that print surprise instead of the original functionality.
    :param _function: The original function.
    :return: Wrapper, basically None.
    """
    def wrapper(*_args, **_kwargs):
        """
        Prints 'surprise!'.
        :param _args: Multiple arguments.
        :param _kwargs: Multiple keyword arguments.
        :return: None.
        """
        print("surprise!")
        return None
    return wrapper


@surprise
def times(number: int):
    """
    Driver function to test the program.
    :param number: Number - integer.
    :return: The number times 2.
    """
    return number*2


"""Should print 'surprise!'. """
times(2)
