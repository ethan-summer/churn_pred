import pandas as pd
#TODO：这个文件里有bug，bug描述 当我在backend目录执行python ./prediction_service/model/main.py --test_file_path ./prediction_service/model/input_test/churn_test.csv --key 12345678 --model xgboost --encrypt_data时
#是正确的，在input_test生成churn_test_encrypt.csv，但是执行python ./prediction_service/model/main.py --encrypt_file_path ./prediction_service/model/input_test/churn_test_encrypt.csv --key 12345678  --decrypt_data时
#生成的文件不再input_test的文件夹里，需要修复 我需要在backend目录下执行python ./prediction_service/model/main.py --encrypt_file_path ./prediction_service/model/input_test/churn_test_encrypt.csv --key 12345678  --decrypt_data
#生成churn_test_encrypt_to_encrypt.csv文件 并在这个input_test目录里

# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad

import argparse
import base64

key = b'abcdefgh'#加密key  动态数据

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(str(plaintext).encode('utf-8'), DES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return encrypted

def des_decrypt(encrypted_data_base64, key):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted_data_padded = base64.b64decode(encrypted_data_base64)
        decrypted_padded_data = cipher.decrypt(encrypted_data_padded)
        decrypted_data = unpad(decrypted_padded_data, DES.block_size)
        #打印decrypted_data的类型
        print(decrypted_data)
        # 确保解密后得到的是一个纯数字字符串
        decrypted_string = decrypted_data.decode('utf-8')
        print(decrypted_string)
        if not decrypted_string.isdigit():
            print(f"Decrypted data is not a digit string: {decrypted_string}")
            return None
        return int(decrypted_string)
    except Exception as e:
        print(f"Error occurred during decryption or conversion: {e}")
        return None 

# def encrypt_csv_column(file_path, key):#加密
#     df = pd.read_csv(file_path)

#     df["id"] = df["id"].apply(lambda x: base64.b64encode(des_encrypt(x, key)).decode('utf-8'))
    
#     df.to_csv(file_path, index=False)
#修改的文件 加密后保存到input_test目录
def encrypt_csv_column(file_path, key):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    
    # 加密'id'列
    df["id"] = df["id"].apply(lambda x: base64.b64encode(des_encrypt(x, key)).decode('utf-8'))
    
    # 指定导出的路径和文件名
    output_file_path = './prediction_service/model/input_test/churn_test_encrypt.csv'
    
    # 导出到CSV，不包括索引
    df.to_csv(output_file_path, index=False)

def decrypt_csv_column(file_path,key):#解密
    df = pd.read_csv(file_path)
    try:
        df["id"] = df["id"].apply(lambda x: des_decrypt(x, key))
    except Exception as e:
            print(f"Error occurred: {e}")
            return False
    # 指定导出的路径和文件名
    df.to_csv(file_path, index=False)
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--test_file_path', type=str, default='input_test/churn_test.csv',
                        help='test dataset ')
    args = parser.parse_args()
    decrypt_csv_column(args.test_file_path, key)


