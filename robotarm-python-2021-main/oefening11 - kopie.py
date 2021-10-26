from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:

for stapelBlokken in range(10):
    robotArm.moveRight()

for stapelBlokken in range(10):
    if robotArm.grab() and robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()

    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()