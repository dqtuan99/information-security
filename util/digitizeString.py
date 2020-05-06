# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:04:48 2020

@author: Do Quang Tuan
"""

def digitizeString(text):
    assert(type(text) is str)
    text = text.lower()
    length = len(text)
    digits = 0
    
    for char in text:
        length -= 1
        char_order = ord(char) - ord('a')
        digits += (char_order * 26**length)
    
    return digits
    