import os
import time
print("Cozmo Assistant: WELCOME BACK, Shaurya")
test = 0
while True:
    a = input("Command: ")
    if a == "open Chrome":
        print("OPENING CHROME")
        time.sleep(1)
        print("message: success")
        os.system('start Chrome')
    if a == "test code":
        test += 1
        print("test " + str(test))
        g = ""
        while True:
            f = input("")
            g += f
            g += "\n"
            if f == "":
                break
        f = open('RUNNER.py','w')
        f.write(g + "\ninput('Press enter to Finish')")
        f.close()
        os.system("start RUNNER.py")
    if a == "DrillKill!":
        quit()
    if a == "add":
        frst = input()
        scnd = input()
        print(int(frst)+int(scnd))
    if a == "subtract":
        frst = input()
        scnd = input()
        print(int(frst)-int(scnd))
    if a == "multiply":
        frst = input()
        scnd = input()
        print(int(frst)*int(scnd))
    if a == "divide":
        frst = input()
        scnd = input()
        print(int(frst)/int(scnd))
    if a == "store info":
        go = input()
        hy = go
    if a == "give info":
        print(hy)
