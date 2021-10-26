from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:

for stapelBlokken in range(9):
    robotArm.moveRight() 

for stapelBlokken in range(10):
    if robotArm.grab() and robotArm.scan() == 'red':
        for i in range(10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(stapelBlokken):
            robotArm.moveLeft()

    else:
        robotArm.drop()
    
    robotArm.moveLeft()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()