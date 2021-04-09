"""SHA512 helper"""

from Crypto.Hash import SHA512
from typing import BinaryIO


def hash(input_stream: BinaryIO) -> bytes:
    """Compute the SHA512 hash value

    :param input_stream: Input stream
    :return: SHA512 hash
    """
    hasher = SHA512.new()

    while True:
        buffer = input_stream.read(4096)
        if not buffer:
            break
        hasher.update(buffer)
    return hasher.digest()
