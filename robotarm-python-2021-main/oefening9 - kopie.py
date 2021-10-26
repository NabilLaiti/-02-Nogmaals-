from RobotArm import RobotArm


robotArm = RobotArm('exercise 9')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:

for stapelBlokken in range(1, 5):
    for i in range(stapelBlokken):
        robotArm.grab()

        for moveRight in range(5):
            robotArm.moveRight()

        robotArm.drop()

        for moveLeft in range(5):
            robotArm.moveLeft()
        
    robotArm.moveRight()

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()