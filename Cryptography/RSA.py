"""RSA Helper"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from typing import BinaryIO


def generate_key_pair(key_size: int = 4096) -> RSA:
    """Generate a new RSA key pair

    :param key_size: Key size in bits
    :return: RSA key pair
    """
    return RSA.generate(key_size)


def encrypt(key: RSA,
            data: bytes) -> bytes:
    """Encrypt data with RSA key

    :param key: RSA key
    :param data: Data to encrypt
    :return: Encrypted data
    """
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(data)


def decrypt(key: RSA,
            data: bytes) -> bytes:
    """Decrypt data with RSA key

    :param key: RSA key
    :param data: Data to decrypt
    :return: Decrypted data
    """
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(data)


def load_from_pem(input_stream: BinaryIO,
                  password: str = None) -> RSA:
    """Load a RSA key from PEM

    :param input_stream: Input stream
    :param password: PEM password
    :return: RSA key
    """
    pem_content = input_stream.read()
    return RSA.import_key(pem_content, password)


def save_private_key_to_pem(key: RSA,
                            output_stream: BinaryIO,
                            password: str,
                            protection: str = 'PBKDF2WithHMAC-SHA1AndAES256-CBC') -> None:
    """Save private RSA key

    :param key: RSA key
    :param output_stream: Output stream
    :param password: Password
    :param protection: Protection algorithm
    """
    encrypted_key = key.export_key(passphrase=password, pkcs=8, protection=protection)
    output_stream.write(encrypted_key)


def save_public_key_to_pem(key: RSA,
                           output_stream: BinaryIO) -> None:
    """Save public RSA key

    :param key: RSA key
    :param output_stream: Output stream
    """
    key_content = key.publickey().export_key()
    output_stream.write(key_content)
