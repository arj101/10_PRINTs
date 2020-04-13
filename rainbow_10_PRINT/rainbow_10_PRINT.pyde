x = 0
y = 0
spacing = 10
xoff = 0


def setup():
    size(1000,650)
    background(25)
    colorMode(HSB,360,100,100,1)
    
def draw():
    global spacing,x,y,yoff,xoff
    
    if y < height:
        

        strokeWeight(3)
        stroke(xoff,100,100)
        
        if random(1) < 0.5:
            line(x,y,x + spacing, y + spacing)
        else:
            line(x + spacing,y,x,y + spacing)
        
        x += spacing
 
        xoff += 360/(width/spacing)
   
        if x > width:
            xoff = 0
            x = 0
            y += spacing


            
            
        
    else:
        save("10print" + str(floor(random(1000))) + ".png")
        print("complete")
        noLoop()
