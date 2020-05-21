import math as mt

def sieveEratosthen(n):
    '''
    Sàng nguyên tố, lưu lại các giá trị nguyên tố nhở hơn n
    :param n:
    :return:
    '''
    prime=[True for i in range(n+1)]
    p=2

    while p*p <n:
        if prime[p]:
            for i in range(p*p, n+1,p):
                prime[i]=False
        p+=1

    string_format= '\n'.join([str(i) for i,val in enumerate(prime) if val and i>=2])
    with open("prime_number/prime_"+ str(n)+".txt",'w') as f:
        f.write(string_format)

# sieveEratosthen(10000000)

def module_pow(a,b,m):
    '''
    hàm tính modul m của hàm mũ
    :param a:
    :param b:
    :param m: Cơ số chia module
    :return:
    '''
    if b==0:
        return 1
    if b==1:
        return a
    w= module_pow(a,b//2,m)
    w= (w*w) % m
    if b%2==1:
        w=(w*a)%m
    return w

def ext_gcd(a,b):
    '''
    hàm tính gcd mở rộng
    :param a:
    :param b:
    :return: ước chung lớn nhất và giá trị
    '''
    m,n= a,b
    xm, ym=1,0
    xn,yn=0,1
    while n!=0 :
        q= m//n
        r=m%n
        xr,yr=xm-q*xn, ym- q*yn
        m,xm,ym=n,xn,yn
        n,xn,yn=r,xr,yr

    return m, xm%b



