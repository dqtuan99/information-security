# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:47:55 2020

@author: Do Quang Tuan
"""
from modular.extendedGCD import extendedGCD
from prime.isPrime import isPrime

def modularInverse(a, n):
    assert(extendedGCD(a, n) == 1)
        
    s = 0
    t = 1
    r = n    
    old_s = 1
    old_t = 0
    old_r = a
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    if old_s < 0:
        old_s = n + old_s
        
    return old_s