"""AES helper"""

from .Padding import encrypt_pad_pkcs7, decrypt_unpad_pkcs7
from Crypto.Cipher import AES
from typing import BinaryIO

KEY_SIZE = 32
IV_SIZE = 16


def encrypt(input_stream: BinaryIO,
            output_stream: BinaryIO,
            key: bytes,
            iv: bytes) -> None:
    """Encrypt data with AES-256-CBC-PKCS7

    :param input_stream: Input stream to encrypt
    :param output_stream: Output stream
    :param key: Key
    :param iv: IV
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypt_pad_pkcs7(input_stream, output_stream, cipher)


def decrypt(input_stream: BinaryIO,
            output_stream: BinaryIO,
            key: bytes,
            iv: bytes) -> None:
    """Decrypt data with AES-256-CBC-PKCS7

    :param input_stream: Input stream to decrypt
    :param output_stream: Output stream
    :param key: Key
    :param iv: IV
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypt_unpad_pkcs7(input_stream, output_stream, cipher)
