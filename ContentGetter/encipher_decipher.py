"""
Given an information, encrypt and decrypt using the given key
"""

from cryptography.fernet import Fernet
import os

def encrypt(information, key):
    """encrypt information and return as string"""
    f = Fernet(key)
    information_bytes = str_to_bytes(information) 
    encrypted_info = f.encrypt(information_bytes) #<--- returns bytes
    encrypted_info = bytes_to_str(encrypted_info) #<--- to save in json requires str not bytes
    return encrypted_info

def decrypt(information, key):
    """decrypt information and return as string"""
    f = Fernet(key)
    information_bytes = str_to_bytes(information)
    decrypted_info = f.decrypt(information_bytes) #<--- returns bytes
    decrypted_info = bytes_to_str(decrypted_info) #<--- converts to string
    return decrypted_info

def bytes_to_str(byte_stuff):
    """Convert bytes to string"""
    return byte_stuff.decode('utf-8')

def str_to_bytes(str_stuff):
    """Converts string to bytes"""
    return bytes(str_stuff, 'utf-8') # or str_stuff.encode('utf-8')

def main():
    user_input = input("Please enter the information you want to encrypt:> ")
    # randomly generate a key from cryptography
    key_test = Fernet.generate_key()
    encrypted = encrypt(user_input, key_test)
    print("Encrypted input = {}".format(encrypted))

    decrypted = decrypt(encrypted, key_test)
    print("Decrypted input = {}".format(decrypted))
    print("Are the original information same as the decrypted?: >{}".format(user_input == decrypted))

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Current location of this file = {}".format(dir_path))
    cwd = os.getcwd()
    print("CWD = {}".format(cwd))

if __name__ == '__main__':
    main()
