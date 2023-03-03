#Create parent class Ball
class Ball:
  #Old roll method
  def roll(self):
    print("Ball's roll")

#Create a non-rollable class
class Cube:
  def notRoll():
    print("I can't roll!")
	
def rollIt(rollable):
  if(hasattr(rollable, "roll")):
    rollable.roll()
  else:
    print("Object not rollable!")

#Create a new instance of a ball
ball = Ball()

#Create a new instance of a cube
cube = Cube()

#Call rollIt with each object
rollIt(ball)
rollIt(cube)