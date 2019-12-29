t=0
def setup():
    size(600,600)
    colorMode(HSB)

def draw():
    global t
    background(255)
    translate(width/2,height/2)
  #  rotate(radians(t))
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+2*i*360/90))
        stroke(3*i,255,255)
        equilateral(100)
        popMatrix()
     #   rotate(radians(360/90))
    t+=0.5
    
def equilateral(length):
    noFill()
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
    
