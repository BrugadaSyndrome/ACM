import sys
import math

'''
def fib(A, B, C, Y):
    print '{0}+{1}={2} A:{5} B:{6}'.format(A, B, A+B, A>=1000000000, B>=1000000000)
    #if (A>=1000000000):
    #    A %= 1000000000
    #if (B>=1000000000):
    #   B %= 1000000000

    
    if (C == Y):
        return (A+1)%1000000000
    else:
        return A + fib(B%1000000000, (A+B)%1000000000, C+1, Y)
'''

# Iterative Fibonacci with 1B upper limmit
def fib(A, B, C, Y):
    T = 1
    while (C <= Y):
        T = (A + B)%1000000000
        A = B%1000000000
        B = T%1000000000
        C+=1
    return T

def mod_pow(base, exponent, modulus):
    if (modulus == 1):
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def Binet(N):
    phi = (1 + 5 ** 0.5) / 2
    #A = mod_pow(phi, N, 1000000000)
    #B = mod_pow(-phi, -N, 1000000000)
    A = pow(phi, N)
    B = pow(-1*phi, -N)
    return (A - B) / 5 ** 0.5

def main():
    cases = int(sys.stdin.readline().strip())
    
    for c in range(cases):
        K, Y = sys.stdin.readline().strip().split()
        K = int(K)
        Y = int(Y)
        print K, int(Binet(Y)) #fib(1, 1, 3, Y)
        print '====='

main()
