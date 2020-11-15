import time
try:
    Diaryw = open('Diary.txt','x')
except FileExistsError:
    Diaryw = open('Diary.txt','a')
    a = ""
    b = input("Do you want to see the previous updates you did to your Diary?Y of for yes and N for no")
    if b == 'y':
        Diaryw.close()
        Diaryw = open('Diary.txt','rt')
        print("\n"+Diaryw.read() + "\n")
        Diaryw.close()
        Diaryw = open('Diary.txt','a')
    c = input("Do you want to erase the diary?y for yes and n for no")
    if c == 'y':
        Diaryw.close()
        Diaryw = open('Diary.txt','w')
        Diaryw.write('')
        Diaryw.close()
        Diaryw = open('Diary.txt','a')
    a = input(time.ctime() + "\nDear Diary\n")
    Diaryw.write("\n"+time.ctime() + "\nDear Diary\n" + a)
    Diaryw.close()


    
    
    
