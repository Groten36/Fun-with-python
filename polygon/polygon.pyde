def setup():
    size(600,600)

def draw():
    translate(width/2,height/2)
    polygon(120,100)
    
def polygon(n,edgeLength):
    beginShape()
    for i in range(n):
        vertex(100*cos(radians((360/n)*i)),100*sin(radians((360/n)*i)))    
    endShape(CLOSE)
