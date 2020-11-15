#_________________________________________________________________________________________________________________________________________________________________________
import random
team1 = input("name of the team batting?")
team2 = input("name of the team bowling?")
a = int(input("How many runs to make?"))
b = input("In how many balls?")
list1 = []
if int(b) * 6 >= int(a):
    list1.append(str(6) + "'s")
    if int(b) * 4 >= int(a):
        list1.append(str(4) + "'s")
        if int(b) * 2 >= int(a):
            list1.append(str(2) + "'s")
print(team1 + " can win by " + str(list(list1)))
list1 = []
i = 0
while i != int(b):
    if int(b) * 2 >= int(a):
        list1.append(str(2))
        int(a)
        a -= 2
    elif int(b) * 4 >= int(a):
        list1.append(str(4))
        int(a)
        a -= 4
    elif int(b) * 6 >= int(a):
        list1.append(str(6))
        int(a)
        a -= 6
    if a <= 0:
        break
    i += 1
random.shuffle(list1)
print(team1 + " can win a by minimum of " + str(list1) + " in " + str(len(list1)) + " balls")
