from math import sqrt
#This program is meant to be a little more itermediate 
#Creating a ball class
class Ball:
  x = 0
  y = 0
  z = 0
   
  #Ball constructor
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  #Ball method
  def move(self):
    self.x += 1
    self.y += 1
    self.z += 1
  
#Create a new instance of Ball  
ball = Ball(0, 0, 0)

#Loop 32 times
for i in range(32):
  #Format string for easy printing.
  print("Ball Position: x=%d, y=%d, z=%d" % (ball.x, ball.y, ball.z))
  #A single function call instead of three
  ball.move()
	
#Print the distance from the start position
#Uses the Pythagorean theorem
print("\nThe ball ended up %d meters away from where it started." % sqrt(ball.x**2 + ball.y**2 + ball.z**2))