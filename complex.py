from math import sqrt

def add(u,v):
    return [u[0]+v[0],u[1]+v[1]]
    
def mul(u,v):
    return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(u):
    return sqrt(u[0]**2+u[1]**2)
    