one1 = None
global a
global v
def Ask():
    global a
    global v
    a = int(input("amount given : "))
    v = int(input("value (NOTE : Unit in which value is needed) : "))
while True:
    d = input("Direct Valuation or Inverse Valuation? D/I : ")
    if d == "exit":
        break

    form = input("FORMAT : ")
    if form == "normal":
        Ask()
        while True:
            if d == "D":
                one = int((v/a))
            if d == "I":
                one = int((v*a))
            am = input("Amount : ")
            if am == "":
                break
            if d == "I":
                print(int(int(one)/int(am)))
            if d == "D":
                print(int(int(one)*int(am)))
    if form == "together":
        Ask()
        if d == "D":
            one = int((v/a))
        if d == "I":
            one = int((v*a))
        a = int(input("amount given : "))
        if d == "D":
            one1 = int((v/a))
        if d == "I":
            one1 = int((v*a))
        while True:
            am = input("Amount 1 : ")
            if am == "":
                break
            am1 = input("Amount 2 : ")
            if d == "I":
                print(int(int(one)/int(am)) + int(int(one1)/int(am1)))
            if d == "D":
                print(int(int(one)*int(am)) + int(int(one1)*int(am1)))
    if d == "I":
        if form == "times":
            Ask()
            total = int(input("how times/days did it take? : "))
            if d == "I":
                one = int((v*a))
            total = one*int(total)
            Ask()
            if d == "I":
                one1 = int((v*a))
            print(str(int(total/one1)) + " times/days")
quit()    

                  
                  
                  
    
