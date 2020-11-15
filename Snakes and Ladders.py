#____________________________________________________________________________Start_____________________________________________________________________________________
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#----------------------------------------------------------------------Initializing Variables(Start)--------------------------------------------------------------------------
import time
print("Initializing, Please Wait")
time.sleep(5)
print("Welcome to Snakes and Ladders")
player1 = input("player 1's name shall be....")
player2 = input("player 2's name shall be....")
player1_position = 1
player2_position = 1
print("Lets go")
import random
dice_number = random.randint(1,6)
snake_bite = random.randint(1,5)
a = 0
ladder_climb = random.randint(1,5)
b = 0
#--------------------------------------------------------------------------Game_loop(Main)-----------------------------------------------------------------------------------------
while player1_position <= 100 or player2_position <= 100:

    a = 0
    b = 0
#______________________________________________________________________________________________________________________________________________________________________    
#Change dice number
    
    dice_number = random.randint(1,6)
#______________________________________________________________________________________________________________________________________________________________________

#player1's turn
    
    time.sleep(1)
    input(player1 +"'s turn. press enter to roll the dice")
    time.sleep(1)
    print(player1 + " got...")
    time.sleep(2)
    print(dice_number)
    a = dice_number
#______________________________________________________________________________________________________________________________________________________________________    
#Check if dice number is 6, if yes, give the player another chance.
    
    if dice_number == 6:
        dice_number = random.randrange(1,6)
        time.sleep(1)
        input(player1 +"'s turn. press enter to roll the dice")
        time.sleep(1)
        print(player1 + " got...")
        print(dice_number)
        b = dice_number
#______________________________________________________________________________________________________________________________________________________________________        
#Check if player1's dice number does not allow him to go higher than hundred and still win
        
    if (player1_position+(a + b)) > 100:
        player1_position -= (a + b)
    player1_position += a + b
    time.sleep(1)
    print(player1 + " is now at number " + str(player1_position))
#______________________________________________________________________________________________________________________________________________________________________
#Check for player whose position is equal to hundred

    if player1_position == 100:
        break
    elif player2_position == 100:
        break
#______________________________________________________________________________________________________________________________________________________________________
#Change dice number
    
    dice_number = random.randint(1,6)
#______________________________________________________________________________________________________________________________________________________________________
#Check for snake bite being equal to 3,also as probablity, if yes then show the player that he/she was bitten by snake and is now at a lower number than before
    
    if snake_bite == 3:
        time.sleep(1)
        print("...but, Oh no! " + player1 + " got bit by a snake!")
        player1_position -= random.randrange(1,player1_position)
        time.sleep(1)
        print(player1 + " has now sunk down to the depths of number " + str(player1_position) + ". Will he/she be able to recover her numbers to fight again?")
    else:
#______________________________________________________________________________________________________________________________________________________________________        
#if not, try randomizing snake bite chances again
        
        snake_bite = random.randrange(1,5)
    snake_bite = random.randrange(1,5)
#______________________________________________________________________________________________________________________________________________________________________
#Check for player whose number is equal to 100

    if player1_position == 100:
        break
    elif player2_position == 100:
        break

    a = 0
    b = 0
#______________________________________________________________________________________________________________________________________________________________________
#player2's turn

    time.sleep(1)
    input(player2 +"'s turn. press enter to roll the dice")
    time.sleep(1)
    print(player2 + " got...")
    time.sleep(2)
    print(dice_number)
    a = dice_number
#______________________________________________________________________________________________________________________________________________________________________
#Give another chance to the player if dice number is equal to 6

    if dice_number == 6:
        dice_number = random.randrange(1,5)
        time.sleep(1)
        input(player2 +"'s turn. press enter to roll the dice")
        time.sleep(1)
        print(player2 + " got...")
        print(dice_number)
        b = dice_number
#______________________________________________________________________________________________________________________________________________________________________
#Check if player1's dice number does not allow him to go higher than hundred and still win

    if (player2_position+(a + b)) > 100:
        player2_position -= (a + b)
    player2_position += (a+b)
    print(player2 + " is now at number " + str(player2_position))
#______________________________________________________________________________________________________________________________________________________________________
#Change dice number 
    
    dice_number = random.randint(1,6)
#_______________________________________________________________________________________________________________________________________________________________________
#Check for player whose number is equal to 100
    
    if player1_position == 100:
        break
    elif player2_position == 100:
        break
#______________________________________________________________________________________________________________________________________________________________________
#Check for snake bite being equal to 3, if yes then show the player that he/she was bitten by snake and is now at a lower number than before
    
    if snake_bite == 3:
        time.sleep(1)
        print("...but, Oh no! " + player2 + " got bit by a snake!")
        player2_position -= random.randrange(1,player2_position)
        time.sleep(1)
        print(player2 + " has now sunk down to the depths of number " + str(player2_position) + ". Will he/she be able to recover her numbers to fight again?")
    else:
#______________________________________________________________________________________________________________________________________________________________________        
#if not, then try randomizing chances of snake bite again
        
        snake_bite = random.randrange(1,5)
    snake_bite = random.randrange(1,5)
#______________________________________________________________________________________________________________________________________________________________________
#Check for a player whose number is equal to hundred (Man, I'm hungry)
    
    if player1_position >= 100:
        break
    elif player2_position >= 100:
        break
    
    a = 0
    b = 0
#______________________________________________________________________________________________________________________________________________________________________
#player1's turn (Ahhhhh, fresh water always freshens me up!)
    
    time.sleep(1)
    input(player1 +"'s turn. press enter to roll the dice")
    time.sleep(1)
    print(player1 + " got...")
    time.sleep(2)
    print(dice_number)
    a = dice_number
#______________________________________________________________________________________________________________________________________________________________________
#Give the player another chance if dice number is 6
    
    if dice_number == 6:
        dice_number = random.randrange(1,6)
        time.sleep(1)
        input(player1 +"'s turn. press enter to roll the dice")
        time.sleep(1)
        print(player1 + " got...")
        print(dice_number)
        b= dice_number
#______________________________________________________________________________________________________________________________________________________________________        
#Check if player1's dice number does not allow him to go higher than hundred and still win

    if (player1_position+(a + b)) > 100:
        player1_position -= (a + b)
    player1_position += int(dice_number)
    print(player1 + " is now at number " + str(player1_position))

#______________________________________________________________________________________________________________________________________________________________________
#Change dice number
    
    dice_number = random.randint(1,6)
#______________________________________________________________________________________________________________________________________________________________________
#Check for snake bite being equal to 3, if yes then show the player that he/she was bitten by snake and is now at a lower number than he/she was before
    
    if ladder_climb == 3:
        time.sleep(1)
        print("Hooray! " + player1 + " has found ladder. Will " + player2 + " be able to catch up?")
        player1_position = random.randint(player1_position, 99)
        print(player1 + " is now on cloud 9 (actually number " + str(player1_position) + ")")
    else:
        ladder_climb = random.randrange(1,5)
    ladder_climb = random.randrange(1,5)
#______________________________________________________________________________________________________________________________________________________________________
#Check for a player whose number is equal to (Yawns, Why am i doing this again? Oh....right, back to work) 
    
    if player1_position >= 100:
        break
    elif player2_position >= 100:
        break
#______________________________________________________________________________________________________________________________________________________________________
#player2's turn
    
    a = 0
    b = 0
    
    time.sleep(1)
    input(player2 +"'s turn. press enter to roll the dice")
    time.sleep(1)
    print(player2 + " got...")
    time.sleep(2)
    print(dice_number)
    a = dice_number
    if dice_number == 6:
        dice_number = random.randrange(1,5)
        time.sleep(1)
        input(player2 +"'s turn. press enter to roll the dice")
        time.sleep(1)
        print(player2 + " got...")
        print(dice_number)
        b = dice_number
    if (player2_position+(a + b)) > 100:
        player2_position -= (a + b)
    player2_position += (a + b)
    print(player2 + " is now at number " + str(player2_position))
    if player1_position >= 100:
        break
    elif player2_position >= 100:
        break
    dice_number = random.randrange(1,7)
    if player1_position >= 100:
        break
    elif player2_position >= 100:
        break
    if ladder_climb == 3:
        time.sleep(1)
        print("Hooray! " + player2 + " has found ladder. Will " + player1 + " be able to catch up?")
        player2_position = random.randint(player2_position, 99)
        print(player2 + " is now on cloud 9 (actually number " + str(player2_position) + ")")
    else:
        ladder_climb = random.randrange(1,7)
    ladder_climb = random.randrange(1,7)
    if player1_position >= 100:
        break
    elif player2_position >= 100:
        break
#____________________________________________________________________________After Game Loop ends___________________________________________________________________________    
#Congratulate the player who has won the game.(IF ANYBODY SHOULD BE CONGRATULATED FOR MAKING A 270 LINE CODE, IT SHOULD BE MEEE!!!!! (bangs his laptop on table))
    
if player1_position >= 100:
    time.sleep(1)
    print("Heartiest Congratulations " + player1 + "!! You have won the game")
    time.sleep(3)
    
elif player2_position >= 100:
    time.sleep(1)
    print("Heartiest Congratulations " + player2 + "!! You have won the game")
    time.sleep(3)
#___________________________________________________________________________Kill Code(End)_____________________________________________________________________________
print("Click OK")
quit()
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#_________________________________________________________________________________End__________________________________________________________________________________        


#it took 3 days to build this code with spending 2 hrs coding everyday
#copyrights, all rights reserved (Nobody gonna steal even a LETTER of MY CODE!!!!!!!! OR ELSE!!!!!)

    
    
    
