from Rass import *

#making robot Rass object
rass = Rass()

#A loop that goes forever to take commands from kyboard and move the robot
while True:
        print("enter command")
        key = input()
        if key == 'w':
                rass.forwards()
        elif key == 'x':
                rass.stop()
        elif key == 's':
                rass.backwards()
        elif key == 'd':
                rass.right()
        elif key == 'a':
                rass.left()
        elif key == 'z':
                break
        else:
                print("Wrong command! Try again.")

