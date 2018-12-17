import os
from utils import read_int

class Rsa:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d
    
    def decrypt(self, reader, writer):
        length = os.fstat(reader.fileno()).st_size
        pos = reader.tell()

        while pos < length - 32:
            c = pow(read_int(reader), self.d, self.n)
            bytes_arr = c.to_bytes(8, byteorder='big')
            writer.write(bytes_arr)
            pos += 32

        c = pow(read_int(reader), self.d, self.n)
        bytes_arr = c.to_bytes(8, byteorder='big')

        if bytes_arr[7] != 0x08:
            writer.write(bytes_arr[:8 - bytes_arr[7]])

    def encrypt(self, reader, writer):
        writer.write(self.d.to_bytes(32, byteorder='big'))
        writer.write(self.n.to_bytes(32, byteorder='big'))

        length = os.fstat(reader.fileno()).st_size
        pos = reader.tell()

        while pos < length:
            bytes_arr = reader.read(8)

            if len(bytes_arr) < 8:
                l = 8 - len(bytes_arr)
                bytes_arr += l.to_bytes(1, byteorder='big') * l

            writer.write(pow(int.from_bytes(bytes_arr, byteorder='big'), self.e, self.n).to_bytes(32, byteorder='big'))
            pos += 8

        if length % 8 == 0:
            writer.write(pow(int.from_bytes([0x08] * 8, byteorder='big'), self.e, self.n).to_bytes(32, byteorder='big'))            
