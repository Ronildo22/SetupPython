"""
This module contains unit tests for the CaesarCipher class.

The tests verify the functionality of the CaesarCipher class, including
encryption and decryption of text, as well as handling of unsupported
characters.
"""

from src.caesar_cipher import CaesarCipher


def test_encript_caesar_cipher_with_word_exists_in_alphabet():
    """
    Test the encryption of a word that exists in the alphabet.

    Verifies that the CaesarCipher correctly encrypts a given text
    when all characters exist in the defined alphabet.
    """

    caesar_cipher = CaesarCipher(shift_to_right=4)
    word_encript = caesar_cipher.encript("ronildo o melhor de todos")

    assert word_encript == "vsrmphssqiplsvhixshsw"


def test_decript_caesar_cipher_with_word_exists_in_alphabet():
    """
    Test the decryption of a word that exists in the alphabet.

    Verifies that the CaesarCipher correctly decrypts a given text
    when all characters exist in the defined alphabet.
    """

    caesar_cipher = CaesarCipher(shift_to_right=4)
    word_encript = caesar_cipher.encript("ronildo o melhor de todos")

    word_decript = caesar_cipher.decript(text=word_encript)
    assert word_decript == "ronildoomelhordetodos"


def test_encript_caesar_cipher_with_word_does_not_exists_in_alphabet():
    """
    Test the encryption of a word that contains characters not in the alphabet.

    Verifies that the CaesarCipher raises an exception when attempting
    to encrypt a text containing unsupported characters.
    """

    caesar_cipher = CaesarCipher(shift_to_right=4)

    try:
        caesar_cipher.encript(
            "ronildo o melronildo o melhor de todos 123ronildo "
            "o melhor de todos 123ronildo o melhor de todos "
            "123ronildo o melhor de todos 123"
            "ronildo o melhor de todos 123hor de todos 123"
        )
    except Exception as e:
        assert str(e) == "Valor não encontrado no alfabeto"


def test_decript_caesar_cipher_with_word_does_not_exists_in_alphabet():
    """
    Test the decryption of a word that contains characters not in the alphabet.

    Verifies that the CaesarCipher raises an exception when attempting
    to decrypt a text containing unsupported characters.
    """

    caesar_cipher = CaesarCipher(shift_to_right=4)

    try:
        caesar_cipher.decript("ronildo o @# de todos 123")
    except Exception as e:
        assert str(e) == "Valor não encontrado no alfabeto"
