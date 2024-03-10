def foo(greeting="Hello world!"):
    """Foo function description ... bla bla text.

    :param a: great parameter, very useful
    :type a: int
    :param c: _description_, defaults to [1,2]
    :type c: list, optional
    :raises AssertionError: _description_
    :return: Returns 0 if everything's ok.
    :rtype: int
    """

    print(f"This is foo function. {greeting}")
    return 0


if __name__ == "__main__":
    foo()
