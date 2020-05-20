# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:24:26 2020

@author: Do Quang Tuan
"""

import random
from util.generatePrime import generateSophieGermainPrime
from modular.modularInverse import modularInverse
from prime.primitiveRoot import *
from util.digitizeString import digitizeString

def Chaum_vanAntverpenSignatureSolver(p_range, alpha_range, message):
    p_left, p_right = p_range
    alpha_left, alpha_right = alpha_range
    
    p = generateSophieGermainPrime(p_left, p_right)[0]
    q = (p - 1)//2
    
    primitive = getPrimitiveRootList(p)[1]
    primitive = random.choice(list(filter(lambda x: alpha_left < x and x < alpha_right, primitive)))
    alpha = primitive**2 % p
    
    a = random.randint(1, q-1)
    beta = pow(alpha, a, p)
    
    x = digitizeString(message)
    y = signature = pow(x, a, p)
    
    e_range = list(range((q-1)//2, q))
    e1 = random.choice(e_range)
    e_range.remove(e1)
    e2 = random.choice(e_range)
    e_range.remove(e2)
        
    c = pow(y, e1, p) * pow(beta, e2, p) % p
    
    d = pow(c, modularInverse(a, q), p)
    
    verify = pow(x, e1, p) * pow(alpha, e2, p) % p
    if verify != d:
        Chaum_vanAntverpenSignatureSolver(p_range, alpha_range, message)
        return None
    
# =============================================================================
#     f1 = random.choice(e_range)
#     e_range.remove(f1)
#     f2 = random.choice(e_range)
#     
#     C = pow(y, f1, p) * pow(beta, f2, p) % p
#     
#     D = pow(C, modularInverse(a, q), p)
#     
#     temp = pow(x, f1, p) * pow(alpha, f2, p) % p
#     verify2 = (D != temp)
# =============================================================================
    
    
    print('================================================================')
    print('a) Confirmation protocol:')
    print('Generate Sophie Germain prime p = 2q + 1:')
    print(f'p = {p} = 2*{q} + 1; {p} is prime and {q} is prime')
    print(f'Since {primitive} is a primitive root of p={p}, hence {primitive}^2 mod {p} = {alpha} is a generator of group of quadratic residues modulo p={p} and of order of q={q}')
    print(f'Generate a in range [1, q-1={q-1}]. Suppose a={a}, then beta = alpha^a mod p = {alpha}^{a} mod {p} = {beta}')
    print()
    print(f'Public key: (p, alpha, beta) = ({p}, {alpha}, {beta})')
    print(f'Private key: a = {a}')
    print()
    print(f'message = {message} => x = digitize("{message}") mod {p} = {x}')
    print(f'Bob sign the message with the signature y = x^a mod p = {x}^{a} mod {p} = {y} and send the pairs (x, signature) = ({x}, {y}) to Alice')
    print()
    print(f'When receiving the message x, Alice wants to verify the signature y. Suppose Alice generated e1={e1} and e2={e2} in range [1, q-1={q-1}], then she will compute:')
    print(f'c = y^e1 * beta^e2 mod p = {y}^{e1} * {beta}^{e2} mod {p} = {c} and send it to Bob')
    print()
    print('Bob will then compute:')
    print(f'd = c^(a^(-1) mod q) mod p = {c}^({a}^(-1) mod {q}) mod {p} = {d} and send it back to Alice')
    print()
    print('Alice then check Bob\'s response by verifying that:')
    print(f'x^e1 * alpha^e2 mod p = {x}^{e1} * {alpha}^{e2} mod {p} = {verify} = d')
    print(f'Hence, Alice accepted that the signature y={y} is valid for the message x={x}')
# =============================================================================
#     print()
#     print('b) Disavowal protocol:')
#     print('In case when d =/= x^e1 * alpha^e2 mod p, Alice has to consider whether y is a forgery or Bob denies his signature. To evaluate this, Alice continues the verification using the following disavowal protocol:')
# =============================================================================
    print('================================================================\n')
    

message = 'TUA'
print('\nBai 4:')
Chaum_vanAntverpenSignatureSolver((1000, 2000), (400, 500), message)

# =============================================================================
# p_left = 1000
# p_right = 2000
# p = generateSophieGermainPrime(p_left, p_right)[0]
# q = (p - 1)//2
# 
# alpha_left = 400
# alpha_right = 500
# 
# =============================================================================
