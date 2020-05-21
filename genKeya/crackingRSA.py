import math as mt
import genKeya.genKey as g
import ultil.ultility as ut
def crack(n,e, encrypt_file):
    with open(encrypt_file) as f:
        hidden_text= f.read()
    with open('../prime_number/prime_10000000.txt','r') as f:
        primes=[]
        while True:
            i=int(f.readline())
            if i> mt.sqrt(n):
                break
            primes.append(i)
    p,q=0,0
    for prime in primes:
        if n%prime==0:
            p= prime
            q= n//prime
            break
    check, d = ut.ext_gcd(e, (p-1)*(q-1))
    g.decrypt(encrypt_file,n,d)
    # g.decrypt(encrypt_file,n,d)

encrypt= '../data_test/encrypttext/encrypt_text.txt'
crack(50291985611473,3537367708873,encrypt)