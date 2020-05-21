import random as rd
import math as mt
from ultil import ultility as ut
def createKey():
    '''
    hàm tạo khóa
    '''

    #chọn hai số nguyên tố
    with open('../prime_number/prime_10000000.txt','r') as f:
        primes=[int(i) for i in f.read().split('\n')]
    num_primes= len(primes)
    p= primes[rd.randint(0,num_primes)]
    q = primes[rd.randint(0, num_primes)]


    n= p*q
    phi_n = (p - 1)*(q - 1)

    while True:
        e= rd.randint(0,phi_n)
        if mt.gcd(e,phi_n)==1:
            print("giá trị e chọn là :", e)
            break

    # tính khóa bí mật
    check, d= ut.ext_gcd(e,phi_n)
    if check==1:
        print("Tạo khóa thành công:")
        print("giá trị p chọn là :", p)
        print("giá trị q chọn là :", q)
        print("giá trị n chọn là :", n)
        print("giá trị phi_n chọn là :", phi_n)
        print("giá trị e chọn là :", e)
        print("giá trị d chọn là :", d)

        return e,n,d
    else:
        print("tạo khóa thất bại")

def encrypt(data_path, n, e):
    with open(data_path) as f:
        plain_text= f.read()
        print("plaintext=",plain_text)
    x= 0
    for i in plain_text:
        x= x*26 + ord(i)-97

    print(x)
    y= ut.module_pow(x,e,n)
    # y= ut.module_pow(y,d,n)
    print(y)
    result=[]
    while y > 0:
        x_ = y % 26 + 97
        result.append(chr(x_))
        y = y // 26
    result = result[::-1]
    result=''.join(result)
    print ("encode = ",result)

    with open('D:\\PycharmProjects\\CyberSecurityProject\\data_test\\encrypttext\\encrypt_text.txt','w') as f:
        f.write(result)
    return 'D:\\PycharmProjects\\CyberSecurityProject\\data_test\\encrypttext\\encrypt_text.txt'


def decrypt(encode_file, n,d):
    with open(encode_file) as f:
        encrypt_text = f.read()
        print("encode = ",encrypt_text)
    x = 0
    for i in encrypt_text:
        x = x * 26 + ord(i) - 97
    y= ut.module_pow(x,d,n)

    result = []
    while y > 0:
        x_ = y % 26 + 97
        result.append(chr(x_))
        y = y // 26
    result = result[::-1]
    result=''.join(result)
    print(result)

if __name__== "__main__":
    e,n,d=createKey()
    data_path='D:\\PycharmProjects\\CyberSecurityProject\\data_test\\plaintext\\_test1.txt'
    path=encrypt(data_path,n,e)
    decrypt(path,n,d)