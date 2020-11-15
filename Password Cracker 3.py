l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words = []
answer = input("Password : ")
done = False

for a in l:
    if done == False:
        for b in l:
            if done == False:
                for c in l:
                    if done == False:
                        for d in l:
                            words.append(a + b + c + d)
for i in words:
    print(i)
    if i == answer:
        print("Cracked Password : " + i)
