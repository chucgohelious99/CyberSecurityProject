import math as m

MAX_N = 100000  # int(1e19)

spf = [0 for i in range(MAX_N)]


def sieve():
    spf[1] = 1
    for i in range(2, MAX_N):
        spf[i] = i

    for i in range(4, MAX_N, 2):
        spf[i] = 2

    for i in range(3, m.ceil(m.sqrt(MAX_N))):
        if spf[i] == i:
            for j in range(i * i, MAX_N, i):

                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i


def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret


sieve()
spf = list(dict.fromkeys(spf))

# n = int(input())
# print("so nhap vao la: ", n)
# can = m.ceil(m.sqrt(n))
# applicant = [i for i in spf if can > i >= 2]
# for app in applicant:
#     if n % app == 0:
#         print('n=%d * %d' % (app, n / app))
