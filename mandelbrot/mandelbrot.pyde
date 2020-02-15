from math import sqrt

xmin=-2
xmax=2

ymin=-2
ymax=2

rangex=xmax-xmin
rangey=ymax-ymin

def setup():
    global xscl,yscl
    size(800,800)
    colorMode(HSB)
    noStroke()
    xscl=float(rangex)/width
    yscl=float(rangey)/height
    
def draw():
    
    for x in range(width):
        for y in range(height):
            z=[(xmin+x*xscl),(ymin+y*yscl)]
            col=mandelbrot(z,100)
            if col==100:
                fill(0)
            else:
                fill((255-20*col),255,255)
            rect(x,y,1,1)
    
def mandelbrot(z,num):
    count=0
    z1=z
    while count <=num:
        if magnitude(z1)>2.0:
            return count
        z1=add(mul(z1,z1),z)
        count+=1
    return num

def add(u,v):
    return [u[0]+v[0],u[1]+v[1]]
    
def mul(u,v):
    return [u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]]

def magnitude(u):
    return sqrt(u[0]**2+u[1]**2)
