import string


class CaesarCipher:
    """
    A class to perform Caesar Cipher encryption and decryption.
    """

    def __init__(self, shift_to_right: int):
        """
        Initialize the CaesarCipher with a specific shift value.

        Args:
            shift_to_right (int): The number of positions to shift the alphabet to the right.
        """
        self.shift_to_right = shift_to_right
        self.alphabet = string.ascii_lowercase

    def encript(self, text: str) -> str:
        """
        Encrypt the given text using the Caesar Cipher.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """

        word_encript = ""
        for text_item in text.replace(" ", ""):
            index = self.alphabet.find(text_item)

            if index == -1:
                raise Exception("Valor não encontrado no alfabeto")

            index_caesar_cipher = index + self.shift_to_right
            word_caesar_cipher = self.alphabet[index_caesar_cipher]

            word_encript = word_encript + word_caesar_cipher

        return word_encript

    def decript(self, text: str) -> str:
        """
        Decrypt the given text using the Caesar Cipher.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """

        word_decript = ""
        for text_item in text.replace(" ", ""):
            index = self.alphabet.find(text_item)

            if index == -1:
                raise Exception("Valor não encontrado no alfabeto")

            index_caesar_cipher = index - self.shift_to_right
            word_caesar_cipher = self.alphabet[index_caesar_cipher]

            word_decript = word_decript + word_caesar_cipher

        return word_decript
