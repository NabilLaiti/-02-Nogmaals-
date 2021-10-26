from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
# Jouw python instructies zet je vanaf hier:


for rechts in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()