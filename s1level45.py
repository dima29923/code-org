''' s1level45
for (var count3 = 0; count3 < 20; count3++) {
  for (var count2 = 0; count2 < 10; count2++) {
    penColour(colour_random());
    for (var count = 0; count < 4; count++) {
      moveForward(20);
      turnRight(90);
    }
    moveForward(20);
  }
  turnLeft(120);
  turnLeft(90);
}
'''

import turtle
ssunde = turtle.Turtle()
ssunde.pensize(7)
ssunde.pencolor('red')
for count3 in range(20):
    for count2 in range(10):
        for count in range(4):
            ssunde.forward(20)    
            ssunde.right(90)    
        ssunde.forward(20)
    ssunde.left(120)
    ssunde.left(90)
