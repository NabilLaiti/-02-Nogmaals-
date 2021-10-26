from RobotArm import RobotArm


robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:

for stappelblokken in range(1, 12, 2):
    robotArm.grab()

    for moveRight in range(10-stappelblokken):
        robotArm.moveRight()

    robotArm.drop()

    for moveLeft in range(9-stappelblokken):
        robotArm.moveLeft()







    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()