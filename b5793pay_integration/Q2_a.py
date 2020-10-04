import ast
import math
from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA


# s1 = 'cf80cf5858c00cf654cd39644ec66873'
# s2 = '789041040361e1bf4dc3a120e1e1397'
# s3 = '674a611a52d39e462b05acd95f2aab1'

# i1 = int(s1, 16)
# i2 = int(s2, 16)
# i3 = int(s3, 16)

'''

取一对互质的数比如p, q p = 61 q = 53 n = p * q = 61 * 53 = 3233
欧拉n = (p-1) * (q-1) = 60 * 52 = 3120
求e；要求 1 < e < 欧拉n  且 e 和 欧拉n 互质； 数有很多，比如17e = 17求d；
要求  e * d % 欧拉n = 1转化公式 x * e + 欧拉n * y = 1 ； 17x + 3120y = 1 ； 
算出x = 2753，y = -15验证要求  17 * 2753 % 3120 = 1

下面注释部分为 设计RSA的公钥，私钥相关d,n, e的过程：
'''

# print(i1, i2, i3)

# print('n=', 151 * 157)
# print(150 * 156)

# print('e=', 20981)
# print('-'*20)

# x = 0
# y = 0
# 20981*x + 23400*y = 1
# x = (1 - 23400*y)/20981
for i in range(-100000, 100000):
    x = (1 - 23400*i)/20981
    if x.is_integer():
        print('possilbe private d in consideration:', x, 'i=', i)

print('-'*20)
# 97421.0 i= -87350
# 74021.0 i= -66369
# 50621.0 i= -45388
# 27221.0 i= -24407
# 3821.0 i= -3426

# print('d=', 3821)

# message = 88


# private_d = 23
# common_n = 187
# public_e = 7

# private_d = 2753
# common_n = 3233
# public_e = 17

message = 10000
print('message is:', message)
# private_d = 50621
common_n = 23707
public_e = 20981

for name, private_d in [('Alice', 50621), ('Bob',27221), ('Karen',3821)]:
    print('At client side[' + name + '], encrypt with private_d:',private_d)
    s0 = pow(message, private_d) % common_n
    print('encrypt output=', s0)

    print('At bank side, decrypt with public_e:', public_e)
    t0 = pow(s0, public_e) % common_n
    print('decrypt message=', t0)

    if t0 == message:
        print('The bank believes this signature is authentic\n')
    else:
        print('The signature is not passed!')


