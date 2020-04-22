# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:01:06 2020

@author: Do Quang Tuan
"""

import random
from isPrime import isPrime
from primeFactorization import primeFactorization
from modularInverse import modularInverse

def isEllipticCurve(p, a, b):
    if (4 * a**3 + 27 * b**2) % p == 0:
        return False
    return True

def calculateE(p, a, b):
    assert(isPrime(p))
    assert(isEllipticCurve(p, a, b))
    
    Qp = []
    for x in range(1, (p-1)//2 + 1):
        Qp.append(pow(x, 2, p))
        
    f = lambda x: (x**3 + a*x + b) % p
    Ep = []
    for x in range(p):
        if f(x) in Qp:
            index = Qp.index(f(x)) + 1
            y1 = index
            y2 = p - index
            Ep.append((x, y1))
            Ep.append((x, y2))
        elif f(x) == 0:
            Ep.append((x, 0))
    
    return Ep

def addingPoints(P, Q, p):
    if P == 0 and Q == 0:
        return 0
    if P == 0 or Q == 0:
        if P == 0:
            return Q
        if Q == 0:
            return P
    
    xP, yP = P
    xQ, yQ = Q
    
    if xP == xQ and yQ == (p - yP):
        return 0
    
    m = ((yP - yQ) * modularInverse((xP - xQ), p)) % p
    xR = (m**2 - xP - xQ) % p
    yR = (m * (xP - xR) - yP) % p
    
    return (xR, yR)

def doublingPoint(P, p, a):
    if P == 0:
        return 0
    
    xP, yP = P
    
    m = ((3 * xP**2 + a) * modularInverse(2 * yP, p)) % p
    xR = (m**2 - 2 * xP) % p
    yR = (m * (xP - xR) - yP) % p
    
    return (xR, yR)

def bits(P):
    while P:
        yield P & 1
        P >>= 1

def doubleAndAdd(n, P, p, a):
    if n == 1:
        return P
    result = 0
    addend = P
    
    for bit in bits(n):
        if bit == 1:
            result = addingPoints(result, addend, p)
        addend = doublingPoint(addend, p, a)
    
    if result == (0, 0):
        return 0
    
    return result

def findGenerator(Ep, p, a):
    N = len(Ep) + 1
    if isPrime(N):
        return Ep[random.randint(0, len(Ep)-1)]
    n = primeFactorization(N)[0]
    h = N//n
    G = 'temp'    
    visited = [0] * len(Ep)
    
    while G != 0:
        if visited == [1] * len(Ep):
            break
        
        index = random.randint(0, len(Ep)-1)
        if visited[index] == 0:
            visited[index] == 1
        else:
            continue
        
        P = Ep[index]
        G = doubleAndAdd(h, P, p, a)
    
    if G == 0:
        return P
    else:
        return 'error 404 generator not found :<'
        
def findGenerator2(Ep, p, a):
    N = len(Ep) + 1
    n = 0
    index = 0
    while n != N:
        if index >= len(Ep):
            break
        G = Ep[index]
        kG = doublingPoint(G, p, a)
        count = 2
        for k in range(3, N+1):
            kG = addingPoints(kG, G, p)
            count += 1
            if kG == 0:
                break
        if count > n:
            n = count
            print(n)
        index += 1
    
    if index >= len(Ep):
        return "toang"
    
    return G               
    
    
print('\n====================================================================')
print('Bai 1:\n')
a, b, p = -1, 188, 751
G = (0, 376)
Ep = calculateE(p, a, b)
print(f'Ep(a, b) = E_{p:d}({a:d}, {b:d}) =')
print(Ep)
print('kG =')
for k in range(1, 770):
    print(f'k = {k:d}, kG = ' + str(doubleAndAdd(k, G, p, a)))
print('====================================================================\n')

print('\n====================================================================')
print('Bai 2:\n')
ngaysinh = 10
thangsinh = 4
a, b, p = ngaysinh+20, thangsinh+20, 751
while not isEllipticCurve(p, a, b):
    a += 1
Ep = calculateE(p, a, b)
print(f'Ep(a, b) = E_{p:d}({a:d}, {b:d}) =')
print(Ep)
G = findGenerator2(Ep, p, a)
print(f'Phan tu sinh G cua E_{p:d}({a:d}, {b:d}) la:')
print(G)
print('kG =')
for k in range(1, 770):
    print(f'k = {k:d}, kG = ' + str(doubleAndAdd(k, G, p, a)))
print('====================================================================\n')











    
    
    
    
    