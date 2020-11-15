import time
from selenium import webdriver
a = webdriver.Chrome()
a.minimize_window()
a.get('https://ytmp3.cc/en13/')
input1 = a.find_element_by_id('input')
input1.send_keys(input('URL : '))
a.execute_script('document.querySelector("#submit").click();')
time.sleep(3)
a.execute_script('document.querySelector("#buttons > a:nth-child(1)").click()')
