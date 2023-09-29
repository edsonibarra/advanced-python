from functools import wraps


def say_something_else(func):
    """
    A decorator for say_something function
    """
    def wrapper():
        """
        A wrapper that concatenates hello world to result
        """
        result = func()
        result += " hello world "
        return result
    return wrapper


@say_something_else
def say_something():
    """
    A function that says something
    """
    return "something"


def deco_with_wraps(f):
    """
    This decorator uses wraps decorator for wrapper
    """
    @wraps(f)
    def wrapper():
        """
        the wrapper within deco_with_wraps
        """
        print("executing the function")
        print(f())
    return wrapper


@deco_with_wraps
def print_my_name():
    """
    It only prints a name
    """
    return "John"


def example_without_wraps_deocrator():
    """
    Shows that:
    __name__ and __doc__ are from wrapper
    within say_something_else decorator
    so, they're not correct
    """

    print("Example without wraps decorator\n")
    print("result =", say_something())
    print("say_something.__name__ =", say_something.__name__)
    print("say_something.__doc__ =", say_something.__doc__)


def example_with_wraps_decorator():
    """
    Each attribute in print_my_name function
    will be printed out correctly
    """
    
    print("Example with wraps decorator\n")
    print("result =", print_my_name())
    print("print_my_name.__name__ =", print_my_name.__name__)
    print("print_my_name.__doc__ =", print_my_name.__doc__)


def main():
    example_without_wraps_deocrator()
    example_with_wraps_decorator()


if __name__ == "__main__":
    main()
