import atexit
import time

from profilehooks import profile


class Dog:
    @staticmethod
    def bark():
        """
        Method to demonstrate staticmethod decorator, can be called without and instance.
        :return: None.
        """
        print("Woof!")


@profile(immediate=True)
def wait(seconds: int):
    """
    Program just sleeps for amount of seconds provided to demonstrate the profile decorator,
    that issues a report for the function.
    :param seconds: Integer.
    :return: None.
    """
    time.sleep(seconds)


@atexit.register
def do_after():
    """
    Function that executes right before the program exits.
    :return: None.
    """
    print("Program ended.")


Dog.bark()
wait(3)
