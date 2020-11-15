while True:
    no = list(map(int, input("Enter 2 numbers separated by space : ").split()))
    print({"add" : str(no[0]) + " + " + str(no[1]) + " = " + str(no[0]+no[1]),"subtract":str(no[0]) + " - " + str(no[1]) + " = " + str(no[0]-no[1]),"multiply":str(no[0]) + " x " + str(no[1]) + " = "+str(no[0]*no[1]),"divide":str(no[0]) + " ÷ " + str(no[1]) + " = " + str(no[0]/no[1])}[input("What would you like to do with the numbers?(add,subtract,multiply,divide) : ")])
    
