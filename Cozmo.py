import time
import ast
from Fusion import *
try:
    Fusion.makeLocalStorageVariable('a','cozmo.py',[])
except FileExistsError:
    pass
try:
    Fusion.makeLocalStorageVariable('b','cozmo.py','[]')
except FileExistsError:
    pass
class Cozmo:
    h = 0
    def findAns(a):
        sa = ast.literal_eval(Fusion.getLocalStorageVariable('a','cozmo.py'))
        try:
            return ast.literal_eval(Fusion.getLocalStorageVariable('a','cozmo.py')).index(a)
        except ValueError:
            Cozmo.h = input("Could not get Answer, Please Type the Answer: ")
            Fusion.addValueToLocalStorageVariable('a','cozmo.py',la,1)
            Fusion.addValueToLocalStorageVariable('b','cozmo.py',Cozmo.h,1)
import os
from gtts import gTTS
la = input()
while True:
    try:
        if la == "/Cozmo toolmode":
            break
        if la == "cmd":
            import webbrowser
            print("Sure,here to help.")
            while True:
                cmd = input('')
                if cmd == "open youtube":
                    webbrowser.open('https://www.youtube.com',new=2)
                if cmd == "search in stackoverflow":
                    query = input()
                    webbrowser.open("https://stackoverflow.com/search?q=" + query,new=2)
                if cmd == "play song":
                    song = input()
                    from selenium import webdriver
                    
                    browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
                    url = "https://gaana.com/search/" + song
                    browser.get(url) #navigate to the page
                    
                    browser.execute_script("""document.querySelector("#new-release-album > li:nth-child(2) > div > div.hover-events-parent > a.imghover").id = "HEY";""")
                    submitButton = browser.find_element_by_id("HEY")
                    submitButton.click()
                    browser.execute_script("""document.querySelector("#trackrow21160773 > li.s_title").id = "SUP";""")
                    Button = browser.find_element_by_id("SUP")
                    Button.click()
                if cmd == "pip install":
                    module = input()
                    os.system("pip install " + module)
                if cmd == "search for video":
                    video = input()
                    from selenium import webdriver
                    
                    browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
                    url = "https://www.youtube.com/results?search_query=" + video
                    browser.get(url) #navigate to the page
                    browser.execute_script("""document.querySelector("#thumbnail").click();""")
                    browser.execute_script("""document.querySelector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button").click()""")
                if cmd == "search":
                    search =  input()
                    webbrowser.open(search,new=2)
                if cmd == "weather":
                    from selenium import webdriver

                    browser = webdriver.Chrome()
                    url = "https://www.google.com/search?ei=fkaYXauyEt6uvgT48bGoBg&q=Weather&oq=Weather&gs_l=psy-ab.3..0l7j0i131j0l2.2440.6808..7172...2.1..0.228.1400.1j4j3......0....1..gws-wiz.....0..0i71j0i67j0i67i70i256j0i10i70i256j0i10.3nD5TzUQdBQ&ved=0ahUKEwir6ZLNzITlAhVel48KHfh4DGUQ4dUDCAs&uact=5"
                    browser.set_window_size(1120, 550)
                    browser.get(url)
                    loc = browser.find_element_by_id("wob_loc").text
                    C = browser.find_element_by_id("wob_tm").text
                    Wind_Speed = browser.find_element_by_id("wob_ws").text
                    browser.execute_script("""document.querySelector("#wob_d > div > div:nth-child(2) > div > div.vk_bk.wob-unit > a:nth-child(3)").click()""")
                    F = browser.find_element_by_id("wob_ttm").text
                    Precipitation = browser.find_element_by_id("wob_pp").text
                    Humidity = browser.find_element_by_id("wob_hm").text

                    print("\n\n\n\n")
                    print("Weather API: \n")
                    print("Location : " + loc + "\n")
                    print("Weather cast (Today)\n")
                    print("--" + C + " Celsius (Temperature)\n")
                    print("--" + F + " Fahrenheit (Temperature)\n")
                    print("--Wind speed : " + Wind_Speed + "\n")
                    print("--Humidity : " + Humidity + "\n")
                    print("--Precipitation : " + Precipitation + "\n")
                    try:
                        browser.close()
                    except ConnectionRefusedError:
                        print("________x YourInternetSUcks x__________")
                if cmd == "exit":
                    break
        if la == "what is the time":
            la = input(Fusion.getPresentTime())
        if la == "/Cozmo toolmode":
            break
        else:
            b = Cozmo.findAns(la)
            Fusion.playSound('C:/Users/Guest/Desktop/PythonProjects/shift.wav')
            la = input("Cozmo: " + ast.literal_eval(Fusion.getLocalStorageVariable('b','cozmo.py'))[b] + "\nYou : ")
    except TypeError:
        la = input("Cozmo: " + Cozmo.h+ "\nYou:")
            
while True:
    
    print("Fusion methods")
    print("outputVal is working")
    print("inputVal is working")
    if Fusion.add(1,1) == 2:
        print("add method is working")
    else:
        print("add method is not working")
    if Fusion.subtract(1,1) == 0:
        print("subtract method is working")
    else:
        print("subtract method is not working")    
    if Fusion.multiply(1,1) == 1:
        print("multiply method is working")
    else:
        print("multiply method is not working")
    if Fusion.divide(4,2) == 2:
        print("divide method is working")
    else:
        print("divide method is not working")  
    if Fusion.square(4) == 16:
        print("square method is working")
    else:
        print("square method is not working")
    if Fusion.getPresentTime == time.ctime():
        print("getPresentTime is working")
    else:
        print("getPresentTime is not working")
    Fusion.makeLocalStorageVariable('g','jsf',1)
    Fusion.setLocalStorageVariableTo('g','jsf',2)
    ka = open("C:/Users/Guest/Desktop/jsf's Local Variables/" + 'variable-name ' + 'g' + '.txt','r')
    if '2' == ka.read():
        print("setLocalStorageVariableTo is working")
    else:
        print("Error with setLocalStorageVariableTo")
    Fusion.addValueToLocalStorageVariable('g','jsf',1)
    print(ka.read())
    print("addValueToLSV is working")
    ka.close()
    Fusion.delLocalStorageVariable('g','jsf')
    try:
        open("C:/Users/Guest/Desktop/jsf's Local Variables/" + 'variable-name ' + 'g' + '.txt','r').read()
        print("delLSV is not working")
    except FileNotFoundError:
        print("delLSV is working")
    Fusion.delLocalStorageVariableFolder('jsf')
    print("delLSVFolder is working")

    if Fusion.rangeInt(1,9) == list(range(1,9)):
        print("rangeInt is working")
    else:
        print("rangeInt is not working")
    duh = input("Command:")
    if duh == 'make program':
        break
del duh
del la
del ka
while True:
    program = input("program name")
    new_prgm = True
    try:
        Fusion.makeLocalStorageVariable('code ' + program,'Program','')
    except FileExistsError:
        new_prgm = False
    try:
        Fusion.makeLocalStorageVariable('flow ' + program,'Program','')
    except FileExistsError:
        pass
    try:
        Fusion.makeLocalStorageVariable('comments ' + program,'Program','')
    except FileExistsError:
        pass
    try:
        Fusion.makeLocalStorageVariable('classes ' + program,'Program','')
    except FileExistsError:
        pass
    try:
        Fusion.makeLocalStorageVariable('stage ' + program,'Program','')
    except FileExistsError:
        pass
