from Crypto.Cipher import DES
from secrets import token_bytes
import time

key = b')*\x92\xf0W2@\xa7'
print(key)

def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg)
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

file_path = r'C:\Users\amade\.spyder-py3\test.txt'

while True:
    print('Choose one of the following operations:\n\t1- Encrypt\n\t2- Decrypt')
    operation = input('Your choice: ')
    if operation not in ['1', '2']:
        break
    
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        
        if operation == '1':
            # Encrypt
            start = time.time()
            nonce, ciphertext, tag = encrypt(file_bytes)
            with open(file_path, 'wb') as output_file:
                output_file.write(ciphertext)
            end = time.time()                
            print(f'{end - start}')
        else:
            # Decrypt
            start = time.time()
            plaintext = decrypt(nonce, ciphertext, tag)
            b = bytes(plaintext, 'utf-8')
            with open(file_path, 'wb') as output_file:
                output_file.write(b)
            end = time.time()                
            print(f'{end - start}')
    
    
# =============================================================================
#     print(f'Cipher text: {ciphertext}')
#     
#     if not plaintext:
#         print('Message is corrupted!')
#     else:
#         print(f'Plain text: {plaintext}')
# =============================================================================
        
  

