import os
import sys
from cryptography.fernet import Fernet
from encipher_decipher import encrypt, decrypt, str_to_bytes, bytes_to_str
import json
import pathlib
import pyperclip
from content_key_writer import content_key_writer


def get_content(path, filename, account):
    """Get the content, decrypt, and copy to clipboard"""
    # assume the data file is in the same directory
    file_path = os.path.join(pathlib.Path(path), filename)

    with open(file_path, 'r') as f:
        data = json.loads(f.read())

    if account in data.keys():
        # Get the key to decrypt
        key = str_to_bytes(data[account]['key'])
        
        # get the content
        value = data[account]['content']

        result = decrypt(value, key)
        pyperclip.copy(result)
        print("Information copied, please paste on your browser.")
    else:
        print("There is no such KEY in the file")

def main():
    path = "C:/Users/nade/Desktop/randomprojects"
    name = 'content.json'
    account = 'youtube'
    content = 'youtubepassword'
    account2 = 'facebook'
    content2 = 'facebookpassword'
    account3 = 'instagram'
    content3 = 'instagrampassword'

    content_key_writer(path, name, account, content)
    content_key_writer(path, name, account2, content2)
    content_key_writer(path, name, account3, content3)
    new_path = os.path.join(pathlib.Path(path),name)
    with open(new_path) as data_file:
        data = json.loads(data_file.read())
        print(data)   
    
    user_wants = 'facebook'
    print("Copying the pass word from account Facebook")
    get_content(path, name, user_wants)
    print("Should have copied facebookpassword")



if __name__ == '__main__':
    main()
