#code below export all from intermediateball file and is able to immediately utilize the function. The new file is even able to utilize the same print function as the intermediateball
# from intermediateball import Ball <---- import Ball Class 
from intermediateball import *

ball = Ball(0, 5, 10)

print("\nThe ball ended up %d meters away from where it started." % sqrt(ball.x**2 + ball.y**2 + ball.z**2))