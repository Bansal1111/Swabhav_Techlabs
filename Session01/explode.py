def add (a,b):
    print(f'{a: ,.2f}+{b: ,.2f}={a + b : >15,.2f}')
def foo(a,b):
    print(a,b)

shares=(1000.567,1000.567)
add(shares[0],shares[1])
add(*shares)
add(*[1000.567,1000.567])
foo(*'hi')