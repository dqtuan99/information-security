# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:58:09 2020

@author: Do Quang Tuan
"""

from util.generatePrime import generatePrime
from util.digitizeString import digitizeString
from modular.modularInverse import modularInverse

def rsaSolver(pq_digits, e_digits, text):
    p = generatePrime(pq_digits)[0]
    q = generatePrime(pq_digits)[0]
    n = p * q
    r = (p - 1) * (q - 1)
    
    e = generatePrime(e_digits)[0]
    d = modularInverse(e, r)
    
    x = digitizeString(text)
    
    c = pow(x, e, n)
    m = pow(c, d, n)
    
    if x != m:
        rsaSolver(pq_digits, e_digits, text)
        return None
    
    print('\n============================================================')
    print(f'p = {p:d}\nq = {q:d}\n')
    print('n = p * q')
    print(f'= {p:d} * {q:d}')
    print(f'= {n:d}')
    print('r = (p - 1) * (q - 1)')
    print(f'= {p-1:d} * {q-1:d}')
    print(f'= {r:d}\n')
    print(f'e = {e:d}')
    print('d = e^(-1) mod r')
    print(f'= {d:d}\n')
    print(f'x = {x:d}\n')
    print('Encrypt:\n')
    print('c = x^e mod n')
    print(f'= {c:d}\n')
    print('Decrypt:\n')
    print('m = c^d mod n')
    print(f'= {m:d}\n= x')
    print('============================================================\n')

# =============================================================================
# rsaSolver(10, 15, 'DoQuangTuan')
# rsaSolver(20, 30, 'PhongChongDichCorona')
# rsaSolver(50, 80, 'HayChungTayPhongChongDichCorona')
# =============================================================================




