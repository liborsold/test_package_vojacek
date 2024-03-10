def foo(greeting="Hello world!"):
    """Example foo function. Will identify itself and greet everyone.

    Args:
        greeting (str, optional): The greeting string. Defaults to "Hello world!".

    Returns:
        int: 0 if successful
    """
    print(f"This is foo function. {greeting}")
    return 0


if __name__ == "__main__":
    foo()
