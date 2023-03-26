from turtle import *
  
def drawFractal(lengthSide, levels):

    def drawLine(lengthSide):
        forward(lengthSide)
        
    if levels == 0:
        drawLine(lengthSide)
        return
    else:
        lengthSide /= 3.0
        drawFractal(lengthSide, levels-1)
        left(60)
        drawFractal(lengthSide, levels-1)
        right(120)
        drawFractal(lengthSide, levels-1)
        left(60)
        drawFractal(lengthSide, levels-1)

  
if __name__ == "__main__":
    
    level = (int(input("Enter a level: ")))
    length = 200.0   
    speed(200)       
    penup()                     
  
    backward(length/2.0)
         
    pendown()
    
    for i in range(3):    
        drawFractal(length, level)
        right(120)
  
    mainloop()       
    

    
