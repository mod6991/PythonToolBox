"""SHA3 Helper"""

from Crypto.Hash import SHA3_512
from typing import BinaryIO


def hash(input_stream: BinaryIO) -> bytes:
    """Compute the SHA3_512 hash value

    :param input_stream: Input stream
    :return: SHA3_512 hash
    """
    hasher = SHA3_512.new()

    while True:
        buffer = input_stream.read(4096)
        if not buffer:
            break
        hasher.update(buffer)
    return hasher.digest()
