import pandas as pd

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
# from Cryptodome.Cipher import DES
# from Cryptodome.Util.Padding import pad, unpad

import argparse
import base64

key = b'abcdefgh'

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(str(plaintext).encode('utf-8'), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded_text, DES.block_size)
    # return decrypted.decode('utf-8')
    return int(float(decrypted.decode('utf-8'))) 

# def encrypt_csv_column(file_path, key):#加密
#     df = pd.read_csv(file_path)

#     df["id"] = df["id"].apply(lambda x: base64.b64encode(des_encrypt(x, key)).decode('utf-8'))
    
#     df.to_csv(file_path, index=False)
#修改的文件 加密后保存到input_test目录
def encrypt_csv_column(file_path, key):
    
    df = pd.read_csv(file_path)
    
    def encrypt_with_new_key(row):
        new_key = (key + str(int(row['id'])))[-8:]
        new_key = new_key.encode('ascii')
        encrypted_data = des_encrypt(row['pred_result'], new_key)
        return base64.b64encode(encrypted_data).decode('utf-8')
    
    
    df["pred_result"] = df.apply(encrypt_with_new_key, axis=1)
    # df["pred_result"] = df["pred_result"].apply(lambda x: base64.b64encode(des_encrypt(x, key)).decode('utf-8'))
    
    output_file_path = './prediction_service/model/input_test/churn_test_encrypt.csv'
    
    df.to_csv(output_file_path, index=False)

def decrypt_csv_column(file_path,key):
    df = pd.read_csv(file_path)

    def decrypt_with_new_key(row):
        new_key = (key + str(int(row['id'])))[-8:]
        new_key = new_key.encode('ascii')
        decrypted_data = des_decrypt(base64.b64decode(row['pred_result'].encode('utf-8')), new_key)
        return decrypted_data
    
    df["pred_result"] = df.apply(decrypt_with_new_key, axis=1)

    # df["pred_result"] = df["pred_result"].apply(lambda x: des_decrypt(base64.b64decode(x.encode('utf-8')), key))
    df.to_csv(file_path, index=False)
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--test_file_path', type=str, default='input_test/churn_test.csv',
                        help='test dataset ')
    args = parser.parse_args()
    decrypt_csv_column(args.test_file_path, key)


