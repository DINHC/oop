#Create a ball class
#Inheritance: using the parent class in which case is Ball and then creating a child class "BeachBall"
class Ball:
  x = 0
  y = 0
  z = 0

  #A function that moves the player's ball
  def moveBall(self, x = 0, y = 0, z = 0):
    self.x += x
    self.y += y
    self.z += z

#Create a beach ball class
#The beach ball is a ball
class BeachBall(Ball):
  color = "blue"

#Create a new beachBall
beachBall = BeachBall()

#Have the beachBall move/ When runn ing code it calls the first number only 
beachBall.moveBall(6,8,10)

#Print the beach ball's new position
print(beachBall.x)

#Print the beach ball's color
print(beachBall.color)