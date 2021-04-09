from IO.BinaryTlv import BinaryTlvWriter, BinaryTlvReader,\
                         tlv_list_from_bytes, build_tlv_list

with open(r'C:\Temp\pytlv.tlv', 'rb') as file:
    tlv = BinaryTlvReader(file)
    d = tlv.read_all()

    print(d)


s = ''
