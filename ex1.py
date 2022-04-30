def surprise(function):
    """
    Decorator that print surprise instead of the original functionality.
    :param function: The original function
    :return: wrapper, basically None.
    """
    def wrapper(*args, **kwargs):
        """
        Print surprise!
        :param args: multiple arguments
        :param kwargs: multiple keyword arguments
        :return: None
        """
        print("surprise!")
        return None
    return wrapper


@surprise
def times(num):
    return num*2


times(2)

