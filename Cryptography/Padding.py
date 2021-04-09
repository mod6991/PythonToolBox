"""Padding helper for symmetric encryption"""

from Crypto.Util.Padding import pad, unpad
from typing import BinaryIO, Any


def encrypt_pad_pkcs7(input_stream: BinaryIO,
                      output_stream: BinaryIO,
                      cipher: Any,
                      buffer_size: int = 4096) -> None:
    """Encrypt data with the given cipher and pad data with PKCS7

    :param input_stream: Input stream to encrypt
    :param output_stream: Output stream
    :param cipher: Symmetric cipher
    :param buffer_size: Buffer size
    """
    pad_done = False
    while True:
        clear = input_stream.read(buffer_size)

        if not clear:
            break

        # if the length of the data is less than buffer_size, it means
        # that we're at the end of the file -> the last data must be padded
        if len(clear) < buffer_size:
            pad_data = pad(clear, 16, style="pkcs7")
            enc = cipher.encrypt(pad_data)
            output_stream.write(enc)
            pad_done = True
            break
        else:
            enc = cipher.encrypt(clear)
            output_stream.write(enc)

    # if the pad is not done yet, it's because the last data was exactly
    # the size of buffer_size, therefore it was impossible to know if
    # other data could be read or not
    if not pad_done:
        pad_data = pad(b'', 16, style="pkcs7")
        enc = cipher.encrypt(pad_data)
        output_stream.write(enc)


def decrypt_unpad_pkcs7(input_stream: BinaryIO,
                        output_stream: BinaryIO,
                        cipher: Any,
                        buffer_size: int = 4096):
    """Decrypt data with the given cipher and unpad data with PKCS7

    :param input_stream: Input stream to decrypt
    :param output_stream: Output stream
    :param cipher: Symmetric cipher
    :param buffer_size: Buffer size
    """
    backup = None
    while True:
        enc = input_stream.read(buffer_size)

        if not enc:
            # if no more data can be read and if the last buffer is
            # stored, it means that the last data was exactly the size
            # of buffer_size -> unpad
            if backup:
                unpad_data = unpad(backup, 16, style="pkcs7")
                output_stream.write(unpad_data)
            break
        else:
            # if the last buffer is stored, write it to the file
            if backup:
                output_stream.write(backup)
                backup = None

        dec = cipher.decrypt(enc)

        # if the length of the data is less than buffer_size, it means
        # that we're at the end of the file -> unpad
        if len(dec) < buffer_size:
            unpad_data = unpad(dec, 16, style="pkcs7")
            output_stream.write(unpad_data)
            break
        else:
            # make a backup of the last buffer because we cannot know
            # if it was the last data of the file
            backup = dec[:]
