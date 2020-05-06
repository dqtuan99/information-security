# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:04:34 2020

@author: Do Quang Tuan
"""

from prime.primeFactorization import primeFactorization
from prime.isPrime import isPrime

def isPrimitiveRoot(g, n):
    assert(isPrime(n))
    assert(0 < g and g < n)
    flag = True
    
    factors = list(set(primeFactorization(n-1)))
    for f in factors:
        if pow(g, (n-1)//f, n) == 1:
            flag = False
            break
    
    return flag

def getPrimitiveRootList(n):
    assert(isPrime(n))
    primitiveRootList = []
    
    for num in range(2, n):
        if isPrimitiveRoot(num, n):
            primitiveRootList.append(num)
            
    return len(primitiveRootList), primitiveRootList
        