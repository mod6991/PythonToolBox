"""SHA256 Helper"""

from Crypto.Hash import SHA256
from typing import BinaryIO


def hash(input_stream: BinaryIO) -> bytes:
    """Compute the SHA256 hash value

    :param input_stream: Input stream
    :return: SHA256 hash
    """
    hasher = SHA256.new()

    while True:
        buffer = input_stream.read(4096)
        if not buffer:
            break
        hasher.update(buffer)
    return hasher.digest()
