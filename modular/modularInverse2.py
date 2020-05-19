# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:48:36 2020

@author: Do Quang Tuan
"""

from prime.primeFactorization import primeFactorization
from prime.isPrime import isPrime

def phi(n):
    p_arr = list(set(primeFactorization(n)))
    product = n
    for p in p_arr:
        product *= (1 - 1/p)
        
    return int(product)

def modularInverse2(a, n):
    if isPrime(n):
        return pow(a, n-2, n)
    
    return pow(a, phi(n)-1, n)