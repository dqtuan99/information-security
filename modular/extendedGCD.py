# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:05:36 2020

@author: Do Quang Tuan
"""

def extendedGCD(a, b):
    s = 0
    t = 1
    r = b
    
    old_s = 1
    old_t = 0
    old_r = a
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_r