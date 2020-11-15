import random
import time
First_Turn = random.randrange(1,2)
Dice_Number = random.randint(1,6)
ai = 0
player = 0
while True:
    
    print("CPU's turn")
    time.sleep(1)
    print("CPU has got...")
    time.sleep(3)
    print(str(Dice_Number))
    ai = Dice_Number
    Dice_Number = random.randint(1,6)
    time.sleep(1)
    input("Your turn, press enter to roll the dice.")
    time.sleep(1)
    print("You got....")
    time.sleep(3)
    print(str(Dice_Number))
    player = Dice_Number
    time.sleep(1)
    if int(player) > int(ai):
        print("You won")
    elif player < ai:
        print("You lose")
    else:
        print("It's a tie!")
        time.sleep(1)
    a = input("""

    Do still want to play? Yes/No

    """)
    if a == "Yes":
        continue
    if a == "No":
        break;
            
print("Click OK to quit")
quit()
