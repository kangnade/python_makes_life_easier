import sys
import os
from cryptography.fernet import Fernet
import json
import pathlib
from encipher_decipher import encrypt, decrypt, bytes_to_str, str_to_bytes 

def content_key_writer(path, filename, account, content):
    """Generate key corresponding to an account, save in json"""
    # make the path a Path object
    path = pathlib.Path(path)
    file_path = os.path.join(path, filename)

    # generate a key using Fernet
    key = Fernet.generate_key()
    # json doesn't support bytes, so convert to string
    key = bytes_to_str(key)

    # with file_path, see if the file exists
    if not os.path.exists(file_path):
        # build the dictionary to hold key and content
        data = {}
        data[account] = {}
        data[account]['key'] = key
        data[account]['content'] = encrypt(content, key)


        # if the file doesn't exist, build the new json file
        with open(file_path, 'w') as f:
            json.dump(data, f)
    else:
        # if the file does exist
        with open(file_path, 'r') as f:
            data = json.load(f)
            data[account] = {} # <--- add the account 
            data[account]['key'] = key
            data[account]['content'] = encrypt(content, key)

        os.remove(file_path) # <--- remove the file and rewrite it
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

def del_account(path, filename, account):
    """Delete the account and its content from the file"""
    path = pathlib.Path(path)
    file_path = os.path.join(path, filename)
    print(file_path) ###
    if not os.path.exists(file_path):
        print("Cannot find the file.")
    else:
        with open(file_path, 'r') as f:
            data = json.load(f)
        data.pop(account)

        os.remove(file_path)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent = 4)

def main():
    path = "C:/Users/nade/Desktop/randomprojects"
    name = 'content.json'
    account = 'youtube'
    content = 'youtubepassword'
    account2 = 'facebook'
    content2 = 'facebookpassword'
    account3 = 'instagram'
    content3 = 'instagrampassword'
    account4 = 'twitter'
    content4 = 'twitterpassword'
    new_path = os.path.join(pathlib.Path(path),name)

    content_key_writer(path, name, account, content)
    content_key_writer(path, name, account2, content2)
    content_key_writer(path, name, account3, content3)
    content_key_writer(path, name, account4, content4)
    
    with open(new_path) as data_file:
        data = data_file.read()
        print(data) 
        data_content = json.loads(data)
    value = data_content['youtube']['content']
    print(value)
    del_account(path, name, account4)
    with open(new_path) as f:
        data_content = f.read()
        print(data_content)

if __name__ == '__main__':
    main()
