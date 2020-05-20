# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:13:44 2020

@author: Do Quang Tuan
"""

import random
from prime.isPrime import isPrime
from prime.primeFactorization import primeFactorization
from modular.modularInverse import modularInverse
from eccAlgorithm import *
from util.digitizeString import digitizeString


def generateKey(p, a, b, G, n, d):
    Q = doubleAndAdd(d, G, p, a)
    print(f'd = {d}')
    print(f'=> Q = dG = {Q}')
    
    return [((p, a, b), G, n, Q), d]

def findPointOrder(p, a, b, G):
    kG = doublingPoint(G, p, a)
    k = 2
    while kG != 0:
        k += 1
        kG = addingPoints(kG, G, p, a)
#        print(f'k = {k}, {k}G = {kG}')
    
    return k

def findPrimeOrderPoint(Ep, p, a, b):
    if isPrime(len(Ep)+1):
        return (Ep[random.randint(0, len(Ep)-1)], len(Ep)+1)
    for G in Ep:
#        print(f'\nG = {G}\n')
        if G[1] == 0:
            continue
        n = findPointOrder(p, a, b, G)
        if isPrime(n):
            return (G, n)
    
    return 'Not Found'
    
def generateSignature(p, a, b, G, n, d, message):
    k = random.randint(1, n-1)
    kG = doubleAndAdd(k, G, p, a)
    r = kG[0] % n
    if r == 0:
        generateSignature(p, a, b, G, n, d, message)
        return None
    hx = digitizeString(message)
    s = (modularInverse(k, n) * (hx + d*r)) % n
    if s == 0:
        generateSignature(p, a, b, G, n, d, message)
        return None
    
    print(f'k = {k}')
    print(f'kG = {kG}')
    print(f'r = x1 mod n = {kG[0]} mod {n}')
    print(f'hx = so hoa "{message}" = {hx}')
    print(f's = (k^(-1) * (hx + dr)) mod n = ({k}^(-1) * ({hx} + {d}*{r})) mod {n}')
    
    return (r, s)

def testSignature(key, signature, n, message):
    public_key, d = key
    Ep, G, _, Q = public_key
    p, a, b = Ep
    r, s = signature
    
    if r not in range(1, n):
        print('r = {r} not in [1, n-1={n-1}]')
        return False    
    print(f'r = {r} in [1, n-1={n-1}]')
    
    if s not in range(1, n):
        print(f's = {s} not in [1, n-1={n-1}]')
        return False    
    print(f's = {s} in [1, n-1={n-1}]')
    
    w = modularInverse(s, n)
    hx = digitizeString(message)
    
    u1 = hx*w % n
    u2 = r*w % n
    x0, y0 = addingPoints(doubleAndAdd(u1, G, p, a), doubleAndAdd(u2, Q, p, a), p, a)
    v = x0 % n
    
    print(f'w = s^(-1) mod n = {s}^(-1) mod {n} = {w}')
    print(f'hx = so hoa "{message}" = {hx}')
    print(f'u1 = hx*w mod n = {hx}*{w} mod {n} = {u1}')
    print(f'u2 = r*w mod n = {r}*{w} mod {n} = {u2}')
    print(f'(x0, y0) = u1G + u2Q = {u1}{G} + {u2}{Q} = ({x0}, {y0})')
    print(f'v = x0 mod n = {x0} mod {n} = {v}')    
    
    if v != r:
        print(f'v={v} not equal r={r} => False')
        return False
    
    print(f'v = r = {v} => True')
    return True
    
def ecdsaSolver(p, a, b, message, random_d=True):
    print('================================================================')
    print(f'ECC: p = {p}, a = {a}, b = {b}')
    print(f'Message = "{message}"')
    Ep = calculateE(p, a, b)
    print(f'order of Ep = {len(Ep)+1}')
    G, n = findPrimeOrderPoint(Ep, p, a, b)
    print(f'G = {G} with order of G: n = {n} is prime')
    if random_d:
        d = random.randint(1, n-1)
    else:
        d = 5
    
    print()
    print('a) Generate ECDSA key:')
    key = generateKey(p, a, b, G, n, d)    
    print(f'Sender private key d = {key[1]}')
    print(f'Sender public key (Ep, G, n, Q) = {key[0]}')
    print()
    print('b) Generate ECDSA signature:')
    signature = generateSignature(p, a, b, G, n, d, message)
    print(f'Signature (r, s) = {signature}')
    print()
    print('c) Test signature:')
    isSignature = testSignature(key, signature, n, message)
    if not isSignature:
        print()
        print('Failed, re-run ECDSA Solver again')
        ecdsaSolver(p, a, b, message, random_d)
        print()
    print('================================================================\n')

print('\nBai 1:')
ecdsaSolver(43, 5, 7, message='TU', random_d=False)

print('\nBai 2:')
ecdsaSolver(751, -1, 188, message='TU', random_d=False)

print('\nBai 3:')
ecdsaSolver(751, -1, 188, message='TU')

# =============================================================================
# p = 43
# a = 5
# b = 7
# Ep = calculateE(p, a, b)
# G, n = findPrimeOrderPoint(Ep, p, a, b)
# d = 5
# message = 'TU'
# 
# key = generateKey(p, a, b, G, n, d)
# print(f'key = {key}')
# print(f'G = {G}, n = {n}')
# signature = generateSignature(p, a, b, G, n, d, message)
# print(f'signature = {signature}')
# isTrue = testSignature(key, signature, n, message)
# print(isTrue)
# =============================================================================



