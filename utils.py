
def read_int(reader):
    return int.from_bytes(reader.read(32), byteorder='big')

def extend_bytes(input, times, b):
    pass