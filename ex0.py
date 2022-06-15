import functools


class InvalidArgumentType(TypeError):
    """Raise for invalid argument that passes to a function."""
    __module__ = 'TypeError'


def type_check(correct_type: type):
    """
    Decorator factory with a decorator that check if the function receives the corrct type of argument.
    :param correct_type: The correct type of argument that need to be passed to the function.
    :return: A decorator.
    """

    def decorator(function):
        """
        Decorator in charge of checking the argument type with a wrapper function.
        :param function: The function that receives the argument.
        :return: The Wrapper function.
        """
        @functools.wraps(function)
        def wrapper(*args):
            """
            Wrapper function that check the type of argument with the correct type that was passed to type_check.
            :param args: Contains any type of argument(int, str, list, etc).
            :raises InvalidArgumentType: If the type received is not the correct type.
            :return: The result of the function with the argument.
            """
            if not isinstance(args[0], correct_type):
                raise InvalidArgumentType("The function: " + function.__name__ + " takes " + correct_type.__name__ +
                                          " and not " + args[0].__class__.__name__)
            result = function(*args)
            return result
        return wrapper
    return decorator


@type_check(int)
def times(number: int):
    """
    Driver function to test the program.
    :param number: Number - integer.
    :return: The number times 2.
    """
    return number*2


"""First call should print 6, and 2nd call should raise an InvalidArgumentType error."""
print(times(3))
print(times('3'))
