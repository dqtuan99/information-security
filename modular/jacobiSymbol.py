# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 09:41:19 2020

@author: Do Quang Tuan
"""

def jacobiSymbol(numerator, denominator, debug=False):
    assert(denominator > numerator > 0 and denominator % 2 == 1)
    jacobi = 1
    
    while numerator != 0: 
        
        while numerator % 2 == 0:            
            numerator /= 2
            if denominator % 8 == 3 or denominator % 8 == 5:
                jacobi = -jacobi
            if debug:
                sign = '+'
                if jacobi == -1:
                    sign = '-'
                print('=', sign, int(numerator), '/', int(denominator))
                
        numerator, denominator = denominator, numerator        
        if numerator % 4 == 3 and denominator % 4 == 3:
            jacobi = -jacobi
        if debug:
                sign = '+'
                if jacobi == -1:
                    sign = '-'
                print('=', sign, int(numerator), '/', int(denominator))
        
        numerator %= denominator
        if debug:
                sign = '+'
                if jacobi == -1:
                    sign = '-'
                print('=', sign, int(numerator), '/', int(denominator))
    
    if denominator == 1:
        return jacobi
    else:
        return 0