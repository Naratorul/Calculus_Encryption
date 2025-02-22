import re
import sympy as sp
from cryptography.fernet import Fernet
import base64
import random
import string

def func1(txt):
    return [int(num) for num in re.findall(r'\d+', txt)]

def func2(msg):
    return [ord(c) for c in msg if ord(c) % 2 == 0]

def func3(nums):  
    x = sp.Symbol('x')  
    expr = sum((n * x**(i + 1)) / (sp.factorial(i + 1) + sp.sin(x) + sp.log(x + 1)) for i, n in enumerate(nums, 1))  
    integral_approx = sum(expr.subs(x, i) for i in range(1, 10))  
    key_num = int(abs(float(integral_approx))) if isinstance(integral_approx, (int, float)) else 42  
    return expr, key_num  

def func4(num):
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    key_base = (str(num) + random_chars).zfill(32)[:32]
    key_bytes = key_base.encode().ljust(32, b'0')
    return base64.urlsafe_b64encode(key_bytes)

def func5(msg, key):
    cipher = Fernet(key)
    return cipher.encrypt(msg.encode())

def func6(encrypted_msg, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_msg).decode()

def main():
    user_msg = input("Message: ")
    nums = func2(user_msg)
    if not nums:
        print("Error.")
        return
    expr, key_num = func3(nums)
    key = func4(key_num)
    print(f"Expression: {expr}")
    print(f"Key: {key.decode()}")
    encrypted_msg = func5(user_msg, key)
    print(f"Encrypted: {encrypted_msg}")
    decrypted_msg = func6(encrypted_msg, key)
    print(f"Decrypted: {decrypted_msg}")

if __name__ == "__main__":
    main()
