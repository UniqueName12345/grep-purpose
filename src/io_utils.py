"""Utility functions for I/O operations."""


def fprint(*args, **kwargs):
    """Wrapper around built-in print for future enhancements."""
    print(*args, **kwargs)


def finput(prompt: str = "") -> str:
    """Wrapper around built-in input for future enhancements."""
    return input(prompt)
