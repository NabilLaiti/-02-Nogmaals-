import time

i = 1

while i <=1:
    print(i,"Maandag")
    i = i + 1
time.sleep(1)
j = 2

while j <=2:
    print(j,"Dinsdag")
    j = j + 2
time.sleep(1)

h = 3

while h <=3:
    print(h,"Woensdag")
    h = h + 3
time.sleep(1)

p = 4

while p <=4:
    print(p,"Donderdag")
    p = p + 4

time.sleep(1)

k = 5

while k <=5:
    print(k,"Vrijdag")
    k = k + 5
time.sleep(1)

a = 6

while a <=6:
    print(a,"Zaterdag")
    a= a + 6
    time.sleep(1)

b = 7

while b <=7:
    print(b,"Zondag")
    time.sleep(1)

    b= b + 7
print("-------------------------------------------------------------------")



print("Kies een dag uit (Cijfer)!")

antwoord = input("1. Maandag\n2. Dinsdag\n3. Woensdag\n4. Donderdag\n5. Vrijdag\n6. Zaterdag\n7. Zondag\n: ")
if antwoord == "1":
    print("Maandag!")
if antwoord == "2":
    print("Dinsdag!")
if antwoord == "3":
    print("Woensdag!")
if antwoord == "4":
    print("Donderdag!")
if antwoord == "5":
    print("Vrijdag")
if antwoord == "6":
    print("Zaterdag")
if antwoord == "7":
    print("Zondag!")
print("-------------------------------------------------------------------")
