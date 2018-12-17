
from rsa import Rsa
from utils import read_int

def rsa():
    image_stream = open('tests/output.jpg', 'wb')

    with open("tests/encrypted.txt", "rb") as encrypted:
        d = read_int(encrypted)
        n = read_int(encrypted)

        if d != 6126098115646990325497939754751346680273131840506753785808675623744493660811:
            raise Exception('Not equal d')

        if n != 11714199531846391552190233593088023207845451372578311171850728357335472002497:
            raise Exception('Not equal n')

        e = 8486391357485896322440256533131770617523773615720428244581337759609685018543

        rsa = Rsa(n, e, d)
        rsa.decrypt(encrypted, image_stream)

    image_stream.close()



if __name__ == "__main__":
    rsa()