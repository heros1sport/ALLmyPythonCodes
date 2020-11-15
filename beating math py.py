while True:
    f = input()
    r = []
    for word in f.split():
       if word.isdigit():
          r.append(int(word))
    r = [r[0] * r[2],r[1] * r[3]]
    for i in range(1,min(r)):
        if r[0] % i == 0 and r[1] % i == 0:
            r[0] /= i
            r[1] /= i
    print(r)
    
