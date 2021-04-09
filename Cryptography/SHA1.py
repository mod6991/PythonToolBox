"""SHA1 Helper"""

from Crypto.Hash import SHA1
from typing import BinaryIO


def hash(input_stream: BinaryIO) -> bytes:
    """Compute the SHA1 hash value

    :param input_stream: Input stream
    :return: SHA1 hash
    """
    hasher = SHA1.new()

    while True:
        buffer = input_stream.read(4096)
        if not buffer:
            break
        hasher.update(buffer)
    return hasher.digest()
