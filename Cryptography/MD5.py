"""MD5 helper"""

from Crypto.Hash import MD5
from typing import BinaryIO


def hash(input_stream: BinaryIO) -> bytes:
    """Compute the MD5 hash value

    :param input_stream: Input stream
    :return: MD5 hash
    """
    hasher = MD5.new()

    while True:
        buffer = input_stream.read(4096)
        if not buffer:
            break
        hasher.update(buffer)
    return hasher.digest()
