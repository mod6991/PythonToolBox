"""PBKDF2 Helper"""

from Crypto.Hash import SHA1
from Crypto.Protocol.KDF import PBKDF2


def generate_key_from_password(nb_bytes: int,
                               password: str,
                               salt: bytes,
                               iterations: int = 10000) -> bytes:
    """Generate a pseudo-random key based on a password and salt

    :param nb_bytes: Number of bytes to generate
    :param password: Password
    :param salt: Salt
    :param iterations: Iterations
    :return: Key
    """
    return PBKDF2(password, salt, nb_bytes, count=iterations, hmac_hash_module=SHA1)
