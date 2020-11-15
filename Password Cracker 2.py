import time
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words = []
answer = input("Password : ")
done = False
a1 = len(l)
a2 = len(l)
a3 = len(l)
a4 = len(l)

b1 = int(len(l) / 2) + 1
b2 = len(l)
b3 = len(l)
b4 = len(l)

c1 = int(len(l) / 2) - 1
c2 = -1
c3 = -1
c4 = -1
for a in l:
    if a1 == 0:
        a1 = len(l)
    a1 -= 1
    if b1 == 0:
        b1 = len(l)
    b1 -= 1
    if c1 == len(l) - 1:
        c1 = -1
    c1 += 1
    if done == False:
        for b in l:
            if a2 == 0:
                a2 = len(l)
            a2 -= 1
            if b2 == 0:
                b2 = len(l)
            b2 -= 1
            if c2 == len(l) - 1:
                c2 = -1
            c2 += 1
            if done == False:
                for c in l:
                    if a3 == 0:
                        a3 = len(l)
                    a3 -= 1
                    if b3 == 0:
                        b3 = len(l)
                    b3 -= 1
                    if c3 == len(l) - 1:
                        c3 = -1
                    c3 += 1
                    if done == False:
                        for d in l:
                            if a4 == 0:
                                a4 = len(l)
                            a4 -= 1
                            if b4 == 0:
                                b4 = len(l)
                            b4 -= 1
                            if c4 == len(l) - 1:
                                c4 = -1
                            c4 += 1
                            print(a + b + c + d + "      " + l[a1] + l[a2] + l[a3] + l[a4] + "     " + l[b1] + l[b2] + l[b3] + l[b4] + "    " + l[c1] + l[c2] + l[c3] + l[c4])
                            if a + b + c + d == answer:
                                done = False
                                break
                            if l[a1] + l[a2] + l[a3] + l[a4] == answer:
                                done = False
                                break
                            if l[b1] + l[b2] + l[b3] + l[b4] == answer:
                                done = False
                                break
                            if l[c1] + l[c2] + l[c3] + l[c4] == answer:
                                done = False
                                break
