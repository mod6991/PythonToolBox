"""Binary helper"""

from struct import pack, unpack
from typing import BinaryIO


def write_byte(stream: BinaryIO, value: int) -> None:
    """Write byte to stream

    :param stream: Output stream
    :param value: byte value
    """
    stream.write(pack('B', value))


def write_bool(stream: BinaryIO, value: bool) -> None:
    """Write bool to stream

    :param stream: Output stream
    :param value: Bool value
    """
    stream.write(pack('?', value))


def write_int16(stream: BinaryIO, value: int) -> None:
    """Write int16 to stream

    :param stream: Output stream
    :param value: int16 value
    """
    stream.write(pack('h', value))


def write_uint16(stream: BinaryIO, value: int) -> None:
    """Write uint16 to stream

    :param stream: Output stream
    :param value: uint16 value
    """
    stream.write(pack('H', value))


def write_int32(stream: BinaryIO, value: int) -> None:
    """Write int32 to stream

    :param stream: Output stream
    :param value: int32 value
    """
    stream.write(pack('i', value))


def write_uint32(stream: BinaryIO, value: int) -> None:
    """Write uint32 to stream

    :param stream: Output stream
    :param value: uint32 value
    """
    stream.write(pack('I', value))


def write_int64(stream: BinaryIO, value: int) -> None:
    """Write int64 to stream

    :param stream: Output stream
    :param value: int64 value
    """
    stream.write(pack('q', value))


def write_uint64(stream: BinaryIO, value: int) -> None:
    """Write uint64 to stream

    :param stream: Output stream
    :param value: uint64 value
    """
    stream.write(pack('Q', value))


def write_float(stream: BinaryIO, value: float) -> None:
    """Write float to stream

    :param stream: Output stream
    :param value: float value
    """
    stream.write(pack('f', value))


def write_double(stream: BinaryIO, value: float) -> None:
    """Write double to stream

    :param stream: Output stream
    :param value: double value
    """
    stream.write(pack('d', value))


def read_byte(stream: BinaryIO) -> int:
    """Read byte from stream

    :param stream: Input stream
    :return: byte value
    """
    data = stream.read(1)
    return unpack('B', data)[0]


def read_bool(stream: BinaryIO) -> bool:
    """Read bool from stream

    :param stream: Input stream
    :return: bool value
    """
    data = stream.read(1)
    return unpack('?', data)[0]


def read_int16(stream: BinaryIO) -> int:
    """Read int16 from stream

    :param stream: Input stream
    :return: int16 value
    """
    data = stream.read(2)
    return unpack('h', data)[0]


def read_uint16(stream: BinaryIO) -> int:
    """Read uint16 from stream

    :param stream: Input stream
    :return: uint16 value
    """
    data = stream.read(2)
    return unpack('H', data)[0]


def read_int32(stream: BinaryIO) -> int:
    """Read int32 from stream

    :param stream: Input stream
    :return: int32 value
    """
    data = stream.read(4)
    return unpack('i', data)[0]


def read_uint32(stream: BinaryIO) -> int:
    """Read uint32 from stream

    :param stream: Input stream
    :return: uint32 value
    """
    data = stream.read(4)
    return unpack('I', data)[0]


def read_int64(stream: BinaryIO) -> int:
    """Read int64 from stream

    :param stream: Input stream
    :return: int64 value
    """
    data = stream.read(8)
    return unpack('q', data)[0]


def read_uint64(stream: BinaryIO) -> int:
    """Read uint64 from stream

    :param stream: Input stream
    :return: uint64 value
    """
    data = stream.read(8)
    return unpack('Q', data)[0]


def read_float(stream: BinaryIO) -> float:
    """Read float from stream

    :param stream: Input stream
    :return: float value
    """
    data = stream.read(4)
    return unpack('f', data)[0]


def read_double(stream: BinaryIO) -> float:
    """Read doubl from stream

    :param stream: Input stream
    :return: doubl value
    """
    data = stream.read(8)
    return unpack('d', data)[0]
