# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:00:53 2020

@author: Do Quang Tuan
"""

def modularExponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    
    c = 1
    for e_prime in range(exponent):
        c = (c * base) % modulus
        
    return c