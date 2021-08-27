"""{{cookiecutter.project_description}}."""


def factorial(integer: int) -> int:
    """Return the factorial of a given integer.

    Args:
        integer (int): the integer whose factorial is going to be calculated

    Returns:
        int: the factorial of the provided integer
    """
    if integer in {0, 1}:
        return 1

    return integer * factorial(integer - 1)
