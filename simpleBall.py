#Creating a Ball class
class Ball:
  #Ball attributes
  x = 0
  y = 0
  z = 0
  
  #Ball constructor. Runs every time a new ball is created
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
#Creating a new instance of a Ball
#Similar looking to a function call
ball = Ball(20, 30, 40)

print("The ball's position: x=%d, y=%d, z=%d" % (ball.x, ball.y, ball.z))