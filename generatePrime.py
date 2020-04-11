# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:01:06 2020

@author: Do Quang Tuan
"""
import random
from isPrime import isPrime
#from modular_exponentiation import modular_exponentiation #co ham pow roi k can nua

def generatePrime(digits, return_size=1):
    assert(digits > 0 and return_size > 0)
    
    appended = 0
    prime_list = []
    
    while appended < return_size:
        n = random.randint(10**(digits-1), 10**digits - 1)
        if isPrime(n):
            prime_list.append(n)
            appended += 1
    
    return prime_list

def generatePrimeAfter(n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    
    while not isPrime(n):
        n += 2
    
    return n
        