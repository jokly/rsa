
from rsa import Rsa
from utils import read_int

def rsa():
    """
    Test RSA
    """

    # Decrypt
    res_image_stream = open('decrypt_rsa.jpg', 'wb')
    with open('tests/encrypted.txt', 'rb') as encrypted:
        d = read_int(encrypted)
        n = read_int(encrypted)

        if d != 6126098115646990325497939754751346680273131840506753785808675623744493660811:
            raise Exception('Not equal d')

        if n != 11714199531846391552190233593088023207845451372578311171850728357335472002497:
            raise Exception('Not equal n')

        e = 8486391357485896322440256533131770617523773615720428244581337759609685018543

        rsa = Rsa(n, e, d)
        rsa.decrypt(encrypted, res_image_stream)

    res_image_stream.close()

    # Encrypt
    res_encrypted = open('encrypted_rsa.txt', 'wb')
    with open('tests/decrypted.jpg', 'rb') as image_stream:
        rsa.encrypt(image_stream, res_encrypted)

    res_encrypted.close()

    # Test encrypt
    test_encrypt = open('test_encrypt.jpg', 'wb')
    with open('encrypted_rsa.txt', 'rb') as res_encrypted:
        d = read_int(res_encrypted)
        n = read_int(res_encrypted)

        if d != 6126098115646990325497939754751346680273131840506753785808675623744493660811:
            raise Exception('Not equal d')

        if n != 11714199531846391552190233593088023207845451372578311171850728357335472002497:
            raise Exception('Not equal n')

        e = 8486391357485896322440256533131770617523773615720428244581337759609685018543

        rsa = Rsa(n, e, d)
        rsa.decrypt(res_encrypted, test_encrypt)

    test_encrypt.close()

if __name__ == "__main__":
    rsa()