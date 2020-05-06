# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:03:51 2020

@author: Do Quang Tuan
"""

import random
from generatePrime import generatePrime
from digitizeString import digitizeString
from primitiveRoot import *
from modularInverse import modularInverse

large_p = [8030402565931338913170389683280894568681757916031794875179951228534244868269784630837071938733360589,
           2449755073722841739142305460627583837452133785913316638094558992383628397683908778183567665592652153,
           9273579819877016871519453719334347258739286654611994964060759749855586686220003151069935049751996081,
           4075437055182159233014167338350714738371092163229484647879789687901724698701701395125902791199924313,
           5896553008117498941572514791107771113051670533930081393569150824142646464511730718503150229602489213,
           1095474788981720861494633572418811282561441496269947020337510232389830316734932092954448082904344803,
           8739175484916890607491885903126273518595660353921461573966781300640086857790330899111484463027500943,
           9669653006076098351036613479590236666835230524444964855404930787046995518177735143055400912459365837,
           8069489254790607179234610095371044176572738772717508381629065067023747474771356382966339895005613759]

def elGamalSolver(p_digits, a_digits, k_digits, text):
    if p_digits == 100:
        p = large_p[random.randint(0, len(large_p)-1)]
    else:
        p = generatePrime(p_digits)[0]
    a = random.randint(10**(a_digits-1), 10**a_digits - 1)
    k = random.randint(10**(k_digits-1), 10**k_digits - 1)
    x = digitizeString(text) % p
    
    alpha = 2
    while not isPrimitiveRoot(alpha, p):
        alpha += 1
    
    beta = pow(alpha, a, p)
    
    e_k = (pow(alpha, k, p), (x % p)*pow(beta, k, p) % p)
    
    temp = pow(e_k[0], a, p)
    d_k = (e_k[1] * pow(temp, p-2, p)) % p
    if d_k != x:
        elGamalSolver(p_digits, a_digits, k_digits, text)
        return None
    
    print('\n===================================================================')
    print(f'p = {p:d}\nalpha = {alpha:d}\na = {a:d}\n')
    print(f'beta = alpha^a mod p = {alpha:d}^{a:d} mod {p:d} = {beta:d}\n')
    print(f'=> public key: ({p:d}, {alpha:d}, {beta:d})\nprivate key: {a:d}\n')
    print(f'x = {text:s}')
    print(f'= {x:d}')
    print(f'k = {k:d}\n')
    print('Encrypt:\n')
    print('e_k (x, k)')
    print(f'= e_k ({x:d}, {k:d})')
    print(f'= (alpha^k, x * beta^k) mod p')
    print(f'= ({alpha:d}^{k:d}, {x:d} * {beta:d}^{k:d}) mod {p:d}')
    print(f'= ({e_k[0]:d}, {e_k[1]:d})\n')
    print('Decrypt:\n')
    print('d_k (e_k1, e_k2)')
    print(f'= d_k ({e_k[0]:d}, {e_k[1]:d})')
    print(f'= e_k2 * (e_k1^a)^-1 mod p')
    print(f'= {e_k[1]:d} * ({e_k[0]:d}^{a:d})^-1 mod {p:d}')
    print(f'= {d_k:d}')
    print('===================================================================\n')
    

elGamalSolver(20, 10, 12, 'VuManhDan')
elGamalSolver(50, 30, 34, 'SongBatDauTuGio')
elGamalSolver(100, 60, 64, 'ToanDanDoanKetChongDich')
