
# -*- coding: utf-8 -*-
'''
Created on Tue May  5 22:47:19 2020

@author: Do Quang Tuan
'''

import numpy as np
from eccAlgorithm import *
from util.digitizeString import digitizeString
from util.generatePrime import generatePrime

def ecElgamalSolver(p, a, b, G, n_B, k, P_M):
    assert(isEllipticCurve(p, a, b))
    
    P_B = doubleAndAdd(n_B, G, p, a)
    kG = doubleAndAdd(k, G, p, a)
    kP_B = doubleAndAdd(k, P_B, p, a)
    P_C = [kG, addingPoints(P_M, kP_B, p)]
    n_Bxk_G = doubleAndAdd(n_B, kG, p, a)
    minus_n_Bxk_G = (n_Bxk_G[0], (-n_Bxk_G[1])%p)
    decoded = addingPoints(addingPoints(P_M, kP_B, p), minus_n_Bxk_G, p)
    
    print('\n=================================================================')
    print('Elliptic curve:')
    print('y^2 = x^3 + ax + b mod p')
    print(f'y^2 = x^3 + {a:d}x + {b:d} mod {p}')
    print(f'E_p(a, b) = E_{p:d}({a:d}, {b:d})')
    print('\nAlice send Bob message:')
    print(f'P_M = {P_M}')
    print(f'Bob secret key: n_B = s = {n_B}')
    print('Bob public key:')
    print(f'P_B = n_B * G = {n_B:d} * {G} = {P_B}')
    print(f'\nAlice generated k = {k:d}')
    print(f'Alice encrypt message using k = {k} and Bob\'s public key P_B = {P_B}:')
    print(f'P_C = [(kG), (P_M + k * P_B)] = [({P_C[0]}), ({P_C[1]})')
    print(f'\nBob received P_C, Bob uses his private key n_B = {n_B:d} to compute P_M:')
    print(f'M = P_M + k * P_B - n_B * kG')
    print(f'M = {addingPoints(P_M, kP_B, p)} - {n_Bxk_G}')
    print(f'M = {addingPoints(P_M, kP_B, p)} + {minus_n_Bxk_G}')
    print(f'M = {decoded}')
    print(f'M == P_M: {decoded == P_M}')
    print('=================================================================\n')
    
    return decoded == P_M

def ecMasseyOmuraSolver(p, a, b, N, M, m_A, m_B):
    M_1 = doubleAndAdd(m_A, M, p, a)
    M_2 = doubleAndAdd(m_B, M_1, p, a)
    

ngaysinh = '10'
thangsinh = '04'
hotensv = 'DOQUANGTUAN'

# Bai 1
# =============================================================================
a = -1
b = 188
p = 751
G = (0, 376)
n_B = s = int(thangsinh + ngaysinh) % 769
k = int(ngaysinh + thangsinh) % 769
P_M = doubleAndAdd(int(ngaysinh)+304, G, p, a)

print('Bai 1:')
ecElgamalSolver(p, a, b, G, n_B, k, P_M)
# =============================================================================

# Bai 2
# =============================================================================
a = int(ngaysinh) + 20
b = int(thangsinh) + 20
p = 751
G = (12, 224)
n_B = generatePrime(int(np.ceil(np.ceil(np.log10(p)/2))))[0]
k = n_B
while (k == n_B):
    k = generatePrime(int(np.ceil(np.ceil(np.log10(p)/2))))[0]
P_M = doubleAndAdd(digitizeString(hotensv)%p, G, p, a)

print('Bai 2:')
ecElgamalSolver(p, a, b, G, n_B, k, P_M)
# =============================================================================

# Bai 3a
# =============================================================================
a = 1
b = 1
p = 14734520141266665763
G = (72, 611)
n_B = 947
k = 97742
P_M = (3683630035316666441, 5525445052974999660)

print('Bai 3a:')
ecElgamalSolver(p, a, b, G, n_B, k, P_M)
# =============================================================================

# Bai 3b
# =============================================================================
a = 1
b = 1
p = 14734520141266665763
G = (72, 611)
n_B = 947
k = 97742
P_M = doubleAndAdd(digitizeString(hotensv)%p, G, p, a)

print('Bai 3b:')
ecElgamalSolver(p, a, b, G, n_B, k, P_M)
# =============================================================================

# Bai 4
# =============================================================================
# =============================================================================
# a = 1
# b = 1
# p = 14734520141266665763
# N = len(calculateE(p, a, b))
# G = (72, 611)
# m_A = generatePrime(int(np.ceil(np.ceil(np.log10(p)/2))))[0]
# m_B = m_A
# while m_B == m_A:
#     m_B = generatePrime(int(np.ceil(np.ceil(np.log10(p)/2))))[0]
# =============================================================================

# =============================================================================











