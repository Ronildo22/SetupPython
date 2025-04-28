"""This module defines custom exceptions for the Caesar Cipher module."""


class ExceptionCaesarCipher(Exception):
    """Base class for exceptions in the Caesar Cipher module."""

    pass


class ValueNotFoundInAlphabet(ExceptionCaesarCipher):
    """Exception raised when a value is not found in the alphabet."""

    pass
