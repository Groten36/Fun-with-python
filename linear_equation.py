def brute_force(a,b,c,d):
    x=-100.0
    while x<100.1:
        if a*x+b==c*x+d:
            return x
        
        x+=0.1
    return "No solution in interval"

def formula(a,b,c,d):
    return (d-b)/(a-c)

a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))
d=float(input("D: "))
print(brute_force(a,b,c,d))
print(formula(a,b,c,d))
        
