#Create parent class Ball
#Polymorphism: ability to call the methods specific to each class being referred while not having to change the code
class Ball:
  posX = 0
  posY = 0
  #Old roll method
  def roll(self):
    print("Ball's roll")

#Create a child class
class BowlingBall(Ball):
  #Override the old roll method
  def roll(self):
    #Call the old method using the super function and calling
    super().roll()
	
#Create a child class
class GolfBall(Ball):
  #Override the old roll method
  def roll(self):
    #Call the old method using the parent class name and passing the self parameter
    Ball.roll(self)

#Create a new instance of a bowling ball
bBall = BowlingBall()

#Create a new instance of a golf ball
gBall = GolfBall()

#Call the bowling ball's roll method
bBall.roll()

#Call the golf ball's roll method
gBall.roll()