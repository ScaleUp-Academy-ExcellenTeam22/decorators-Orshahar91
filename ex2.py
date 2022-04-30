from decorator import decorator


@decorator
def run_twice(function, *args, **kwargs):
    """
    A decorator to run the function it receives twice.
    :param function: The function to run twice.
    :param args: Multiple positional arguments.
    :param kwargs: Multiple keyword arguments.
    :return: The value that the function returns.
    """
    function(*args, **kwargs)
    return function(*args, **kwargs)


@run_twice
def print_hello_world():
    """
    Driver function to test the decorator.
    :return: None.
    """
    print("Hello World!")


"""Should print 'Hellow World!' twice."""
print_hello_world()
