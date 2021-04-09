import io
from Cryptography import RSA

key = RSA.generate_key_pair(2048)

bio = io.BytesIO()

s = ''
