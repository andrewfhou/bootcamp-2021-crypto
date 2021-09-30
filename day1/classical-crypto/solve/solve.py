import base64

binstr = "0110111101101110011001010111001100100000011000010110111001100100001000000111101001100101011100100110111101110011"

hexstr = "636F756E74696E6720696E206865782069732030207468726F7567682066"

b64str = "YmFzZTY0IGRvZXNuJ3QgYWx3YXlzIGVuZCB3aXRoID0sIGJ1dCBpdCdzIGEgdXNlZnVsIHRlbGwK"

# binary to ascii

n = int(binstr, 2)
print(n.to_bytes((n.bit_length() * 7) // 8, "big").decode())

# hex to ascii

print(bytearray.fromhex(hexstr).decode())

# base64 to ascii

b64_bytes = b64str.encode('ascii')
m_bytes = base64.b64decode(b64_bytes)
print(m_bytes.decode('ascii'))

