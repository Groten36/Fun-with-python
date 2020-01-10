
def setup():
    size(600,600)
    noStroke()
    
def draw():
    global t
    background(255)
    translate(width/2,height/2)
    points=[]
    t=0
    while t<100:
        points.append(harmonograph(t))
        t+=0.01
    for i,p in enumerate(points):
        stroke(255,0,0)
        if i<len(points)-1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])
    
    
def harmonograph(t):
    a1=a2=a3=a4=150
    f1,f2,f3,f4=1,2,3,4
    p1,p2,p3,p4=-PI,0,-PI/2,0
    d1,d2,d3,d4=0.0085,0.0030,0.0065,0.0050
    x=a1*cos(f1*t+p1)*exp(-d1*t)+a3*cos(f3*t+p3)*exp(-d3*t)
    y=a2*cos(f2*t+p2)*exp(-d2*t)+a4*cos(f4*t+p4)*exp(-d4*t)
    return [x,y]    
    
