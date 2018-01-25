from Sieve import sieve


def primeFactorsGivenPrimes(n, primes):
    """returns a list of prime factors of n,
    given all possible primes in order."""
    factors = {}
    for p in primes: 
        while n % p == 0:
            n //= p
            factors[p] = factors.get(p,0)+1
        if n < p*p:
            if n > 1:
                factors[n] = factors.get(n,0)+1
            return factors
    return factors

def allFactors(n,pms):
    pfs = primeFactorsGivenPrimes(n,pms)
    ans = []
    def too(p,q):
        a = []
        x=p
        for i in range(q):
            a.append(x)
            x*=p
        return a
    for p in pfs:
        if not ans: ans = too(p,pfs[p])
        else:
            ns = too(p,pfs[p])
            temp = [i*n for i in ans for n in ns]
            ans.extend(temp+ns)
    return ans
    
            
pms = sieve(100000)
bs = sorted(allFactors(1200,pms))
print(bs)
