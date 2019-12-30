t=0
circles=[]
def setup():
    size(600,600)
    
def draw():
    global t, circles
    background(200)
    translate(width/4,height/2)
    noFill()
    stroke(0)
    ellipse(0,0,200,200)
    
    fill(255,0,0)
    x=100*cos(t)
    y=100*sin(t)
    circles.insert(0,y)
    ellipse(x,y,10,10)
    
    stroke(255,255,0)
    line(x,y,200,y)
    fill(255,255,0)
    ellipse(200,y,10,10)
    for i,e in enumerate(circles):
        ellipse(200+i,e,10,10)
    t+=0.05
