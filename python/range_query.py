from random import choices

def build(arr,func):
    N = len(arr)
    ds = {} #2d dic, |keys| = logN, |value| = N
    i = 0
    while 2**i<N:   
        if i==0: ds[i] = arr[:]
        else:
            ds[i] = ds[i-1][:]
            for j in range(N):
                ds[i][j] = ds[i-1][j]
                if j+2**(i-1)<N:
                    ind = int(j+2**(i-1))
                    ds[i][j] = func(ds[i][j],ds[i-1][ind])
        i+=1
    return ds

def query(ds,arr,i,sz,func):
    """query(ds,[1,2,3,4],0,2,max)==2"""
    from math import log2
    p = int(log2(sz)) #for 21, it's 4(2**4==16)
    ans = ds[p][i]
    left = int(sz - int(2**p)) #for 21, its' 5
    if left<=0: return ans
    return func(ans,query(ds,arr,i+2**p,left,func))

#-----------Testing & Benchmarking------------------------------

def build_test(ds,arr,func):
    N = len(arr)
    i = 0
    while 2**i<N:
        for j in range(N):
            ind = int(j+2**i)
            assert ds[i][j] == func(arr[j:ind])
        i+=1

def query_test(ds,arr,func,z=1):
    N = len(arr)
    i = 0

    while i<z:
        a,b = choices(range(N),k=2)
        b+=1
        if a+b>=N: continue
        i+=1
        print(a,b)
        assert func(arr[a:a+b]) == query(ds,arr,a,b,func)

def benchmark(func,z=10):
    from time import clock
    arr = choices(range(1000000),k=100000)
    print("size:",len(arr))
    x = clock()
    ds = build(arr,func)
    y = clock()
    print(f"To build it took :{y-x} secs")
    build_test(ds,arr,func)
    print("No of queries:",z)
    tot,sw = 0,0
    i = 0
    while i<z:
        a,b = choices(range(len(arr)),k=2)
        b+=1
        if a+b>=len(arr): continue
        i+=1
        sw+=b
        x = clock()
        query(ds,arr,a,b,func)
        y = clock()
        tot+=(y-x)
    print(f"took: {tot}, on avg: {tot/z} secs")
    print(f"searched total : {sw}")

benchmark(max)























