import pygame
pygame.init()
from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
a = webdriver.Chrome()
a.minimize_window()
a.get("https://dictation.io/speech")
time.sleep(11)
a.execute_script("""document.querySelector("#speech > div.ql-editor > p:nth-child(2)").innerText = null;""")
time.sleep(6)
a.execute_script("""document.querySelector("#speech > div.ql-editor > p:nth-child(4)").innerText = null;""")
time.sleep(4)
a.execute_script("""document.querySelector("#speech > div.ql-editor > p:nth-child(6)").innerText = null;""")
body = a.find_elements_by_tag_name("body")[0]
a.execute_script("""document.querySelector("#dictation > div.col-lg-7.col-md-8.col-sm-8.col-xs-12 > div > div.action-buttons > div.left.chrome > a > span").click()""")
a.maximize_window()
input("Clicked Allow?")
a.minimize_window()
a.execute_script("""document.querySelector("#dictation > div.col-lg-7.col-md-8.col-sm-8.col-xs-12 > div > div.action-buttons > div.left.chrome > a > span").click()""")
while True:
    try:
        a.execute_script("""document.querySelector("#speech > div.ql-editor > p").innerText = null;""")
    except:
        pass
    input("Start Listening?")
    a.execute_script("""document.querySelector("#dictation > div.col-lg-7.col-md-8.col-sm-8.col-xs-12 > div > div.action-buttons > div.left.chrome > a > span").click()""")
    input("Listening...")
    a.execute_script("""document.querySelector("#dictation > div.col-lg-7.col-md-8.col-sm-8.col-xs-12 > div > div.action-buttons > div.left.chrome > a > span").click()""")
    time.sleep(2)
    b = a.find_element_by_xpath("""/html/body/div[3]/section/div/div/div[2]/div/div[2]/div[1]/p""")
    print(b.text)
    if b.text[1:] == 'how is the weather today':
        a.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        a.get("""https://www.google.com/search?q=how+is+the+weather+today&oq=how+is+the+weather+today&aqs=chrome..69i57.7096j0j7&sourceid=chrome&ie=UTF-8""")
        loc = a.find_element_by_id("wob_loc").text
        C = a.find_element_by_id("wob_tm").text
        Wind_Speed = a.find_element_by_id("wob_ws").text
        a.execute_script("""document.querySelector("#wob_d > div > div:nth-child(2) > div > div.vk_bk.wob-unit > a:nth-child(3)").click()""")
        F = a.find_element_by_id("wob_ttm").text
        Precipitation = a.find_element_by_id("wob_pp").text
        Humidity = a.find_element_by_id("wob_hm").text

        print("\n\n\n\n")
        print("Weather API: \n")
        print("Location : " + loc + "\n")
        print("Weather cast (Today)\n")
        print("--" + C + " Celsius (Temperature)\n")
        print("--" + F + " Fahrenheit (Temperature)\n")
        print("--Wind speed : " + Wind_Speed + "\n")
        print("--Humidity : " + Humidity + "\n")
        print("--Precipitation : " + Precipitation + "\n")
        K = gTTS(loc + ",Today, " + str(C) + " Celsius " + str(F) + " Fahrenheit ")
        K.save('hello.mp3')
        pygame.mixer.music.load('hello.mp3')
        pygame.mixer.music.play(1)
