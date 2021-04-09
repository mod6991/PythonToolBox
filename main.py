from IO.BinaryTlv import BinaryTlvWriter, BinaryTlvReader,\
                         tlv_list_from_bytes, build_tlv_list

with open(r'C:\Temp\pytlv.tlv', 'wb') as file:
    tlv = BinaryTlvWriter(file, 3)
    tlv.write('T01', b'\xff\xfe')
    tlv.write('T02', b'\x00\x02')


s = ''
