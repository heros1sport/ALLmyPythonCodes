a = input("enter name")
f = open(a + '.htm','x')
f.close()
f = open(a + '.htm','a')
b = input("Write HTML code here..")
while True:
    if b == "":
        break
    f.write(b + "\n")
    b  = input("")
f.close()
