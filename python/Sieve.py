
import time 
def sieve(n):
    """THE BEST VERSION"""
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]


#generator version
def prime_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for n in range(2, limit, 2):     # Mark factors non-prime
        a[n] = False
    yield 2
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, 2*i):     # Mark factors non-prime
                a[n] = False

def foo(n):
    from math import sqrt
    nroot = int(sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    sieve = [x for x in sieve if x !=0]
    return sieve

def test(s,f,g):
    from time import clock
    x = clock()
    a = f(s)
    y = clock()
    b = list(g(s))
    z = clock()
    assert a==b
    print(y-x,z-y)

if __name__=='__main__':
    test(8000000,sieve,prime_sieve)
