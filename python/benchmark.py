def test(s,f,g):
    from time import clock
    x = clock()
    a = f(s)
    y = clock()
    b = g(s)
    z = clock()
    assert a==b
    print(y-x,z-y)
