"""DES helper"""

from .Padding import encrypt_pad_pkcs7, decrypt_unpad_pkcs7
from Crypto.Cipher import DES
from typing import BinaryIO

KEY_SIZE = 8
IV_SIZE = 8


def encrypt(input_stream: BinaryIO,
            output_stream: BinaryIO,
            key: bytes,
            iv: bytes) -> None:
    """Encrypt data with DES-CBC-PKCS7

    :param input_stream: Input stream to encrypt
    :param output_stream: Output stream
    :param key: Key
    :param iv: IV
    """
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypt_pad_pkcs7(input_stream, output_stream, cipher)


def decrypt(input_stream: BinaryIO,
            output_stream: BinaryIO,
            key: bytes,
            iv: bytes) -> None:
    """Decrypt data with DES-CBC-PKCS7

    :param input_stream: Input stream to decrypt
    :param output_stream: Output stream
    :param key: Key
    :param iv: IV
    """
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypt_unpad_pkcs7(input_stream, output_stream, cipher)
