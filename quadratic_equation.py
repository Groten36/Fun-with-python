from math import sqrt
def solve(a,b,c):
    x1=(-b+sqrt(b**2-4*a*c))/2*a
    x2=(-b-sqrt(b**2-4*a*c))/2*a
    return x1,x2

a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))
solve(a,b,c)
