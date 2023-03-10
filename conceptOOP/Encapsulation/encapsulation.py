#Create a ball class
#Encapsulation: putting an object such as the player inside of another object
class Ball:
  x = 0
  y = 0
  z = 0

  #A function that moves the player's ball
  def moveBall(self, x = 0, y = 0, z = 0):
    self.x += x
    self.y += y
    self.z += z

#Create a player class
class Player:
  #The player has a ball
  ball = Ball()

  #A function to throw the player's ball
  def throwBall(self):
    #Uses keyword arguments
    self.ball.moveBall(x = 50)

#Create a new player
player = Player()

#Have the player throw his ball
player.throwBall()

#Print the player's ball's new position
print(player.ball.x)