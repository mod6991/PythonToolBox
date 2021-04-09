"""BinaryTlv classes"""
from . import BinaryHelper
from io import BytesIO
from typing import BinaryIO, Optional


class TlvError(Exception):
    pass


def build_tlv_list(values: dict, tag_length: int) -> bytes:
    """Build a tlv list

    :param values: Values to write
    :param tag_length: Tag length for the values
    :return: TLV list bytes
    """
    with BytesIO() as ms:
        tlv = BinaryTlvWriter(ms, tag_length)
        for k, v in values.items():
            tlv.write(k, v)
        ms.seek(0)
        return ms.read()


def tlv_list_from_bytes(data: bytes) -> dict:
    """Read a TLV from bytes

    :param data: Data containing the TLV list
    :return: dict of tag-values
    """
    tlv_list = dict()
    with BytesIO(data) as ms:
        tlv = BinaryTlvReader(ms)
        while True:
            tv = tlv.read()
            if not tv:
                break
            tlv_list[tv.tag] = tv.value

        return tlv_list


class TagValue:
    def __init__(self, tag: str, value: bytes):
        self.tag = tag
        self.value = value


class BinaryTlvWriter:
    def __init__(self, output_stream: BinaryIO, tag_length: int):
        self.output_stream = output_stream
        self.tag_length = tag_length
        self.tags = []

        BinaryHelper.write_byte(self.output_stream, tag_length)

    def write(self, tag: str, value: bytes) -> None:
        """Write TLV into output stream

        :param tag: Tag
        :param value: Value
        """
        if not tag:
            raise TlvError('tag is empty')
        if value is None:
            raise TlvError('value is None')
        if tag in self.tags:
            raise TlvError(f"tag '{tag}' already written")
        else:
            self.tags.append(tag)

        pad_tag = tag.ljust(self.tag_length)
        if len(pad_tag) != self.tag_length:
            raise TlvError('Invalid tag length')

        self.output_stream.write(bytes(pad_tag, 'ascii'))
        BinaryHelper.write_int32(self.output_stream, len(value))
        self.output_stream.write(value)


class BinaryTlvReader:
    def __init__(self, input_stream: BinaryIO):
        self.input_stream = input_stream
        self.tag_length = BinaryHelper.read_byte(self.input_stream)

    def read(self) -> Optional[TagValue]:
        """Read a single TLV from the input stream

        :return: TagValue
        """
        tag_data = self.input_stream.read(self.tag_length)

        if not tag_data:
            return None

        tag = tag_data.decode('ascii').strip()
        value_length = BinaryHelper.read_int32(self.input_stream)
        value = self.input_stream.read(value_length)
        return TagValue(tag, value)

    def read_all(self) -> dict:
        """Read all TLV from the input stream

        :return: dict of tag-values
        """
        self.input_stream.seek(0)
        data = self.input_stream.read()
        return tlv_list_from_bytes(data)
