import os
from utils import read_int

class Rsa:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d
    
    def decrypt(self, reader, writer):
        len = os.fstat(reader.fileno()).st_size
        pos = reader.tell()

        while pos < len - 32:
            c = pow(read_int(reader), self.d, self.n)
            bytes_arr = c.to_bytes(8, byteorder='big')
            writer.write(bytes_arr)
            pos += 32

        c = pow(read_int(reader), self.d, self.n)
        bytes_arr = c.to_bytes(8, byteorder='big')

        if bytes_arr[7] != 0x08:
            writer.write(bytes_arr[:8 - bytes_arr[7]])

            
