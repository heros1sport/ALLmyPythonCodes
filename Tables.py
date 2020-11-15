while True:
    a = input("please type a number to see its table.")
    b = 1
    switch = 1
    while switch < 101:
        product = int(a) * int(b)
        print(str(a) + " x " + str(b) + " = " + str(product))
        b += 1
        switch += 1
        
#creates a table of the given input
    
