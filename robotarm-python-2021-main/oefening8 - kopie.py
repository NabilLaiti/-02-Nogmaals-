from RobotArm import RobotArm



robotArm = RobotArm('exercise 8')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:

for rechts in range(1):
    robotArm.moveRight()

    for anntalblokken in range(7):
        robotArm.grab()

        for rechts2 in range(8):
            robotArm.moveRight()
        robotArm.drop()

        for links in range(8):
            robotArm.moveLeft()
        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()