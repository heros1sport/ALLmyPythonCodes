try:
    import chromedriver_autoinstaller
except:
    os.system("python -m pip install -U chromedriver-autoinstaller")
    import chromedriver_autoinstaller
print(chromedriver_autoinstaller.install())
import time
import os
try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
    from selenium import webdriver
try:
    import pandas as pd
except:
    os.system("pip install pandas")
    import pandas as pd
try: 
    import urllib.request
except:
    os.system("pip install urllib")
    import urllib.request

try:
    from bs4 import BeautifulSoup
except:
    os.system("pip install beautifulsoup4")
    from bs4 import BeautifulSoup





import re
try:
    os.mkdir("J & K Terrorism History DataBase")
    os.mkdir(r"J & K Terrorism History DataBase\Fatalities")
    os.mkdir(r"J & K Terrorism History DataBase\Major Incidents")
    os.mkdir(r"J & K Terrorism History DataBase\Suicide Attacks")
    os.mkdir(r"J & K Terrorism History DataBase\Arm Recovery")
    os.mkdir(r"J & K Terrorism History DataBase\Explosions")
    os.mkdir(r"J & K Terrorism History DataBase\Arrest")
    os.mkdir(r"J & K Terrorism History DataBase\Surrender")
    os.mkdir(r"J & K Terrorism History DataBase\Explosions")
    os.mkdir(r"J & K Terrorism History DataBase\Arrest")
except:
    print("UPDATING GENERATED DATA")
        
browser = webdriver.Chrome()

i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/surrender/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Arrest\arrest.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
time.sleep(3)
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    time.sleep(3)
    try: 
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    try: 
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    time.sleep(3)
    try:
        table = pd.read_html(browser.page_source)[1]
    except:
        break
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Surrender\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/surrender/india-jammukashmir")
    i += 1


# Arrest

i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/arrest/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Arrest\arrest.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
    
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    time.sleep(3)
    try: 
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    try: 
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    try:
        table = pd.read_html(browser.page_source)[1]
    except:
        break
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Arrest\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/arrest/india-jammukashmir")
    i += 1


# Explosions

i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/explosions/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Explosions\explosions.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
    
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    time.sleep(3)
    try: 
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    try: 
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    try:
        table = pd.read_html(browser.page_source)[1]
    except:
        break
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Explosions\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/explosions/india-jammukashmir")
    i += 1


# arms recovery

i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/recovery-of-arms/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Arm Recovery\arms-recovery.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
    
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    time.sleep(3)
    try:
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        pass
    if "*" in year:
        year = year[0:-1]
    try: 
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    try:
        table = pd.read_html(browser.page_source)[1]
    except:
        break
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Arm Recovery\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/recovery-of-arms/india-jammukashmir")
    i += 1


# suicide attacks
browser.get("https://www.satp.org/datasheet-terrorist-attack/suicide-attacks/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Suicide Attacks\suicide-attacks.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
i = 3
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    
    time.sleep(3)
    try:
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    table = pd.read_html(browser.page_source)[1]
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Suicide Attacks\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/suicide-attacks/india-jammukashmir")
    i+=1

# major incidents
i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/major-incidents/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Major Incidents\major-incidents.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    
    time.sleep(3)
    try:
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    try:
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvMajorIncident_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    table = pd.read_html(browser.page_source)[0]
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Major Incidents\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/major-incidents/india-jammukashmir")
    i+=1

# fatalities

i = 3
browser.get("https://www.satp.org/datasheet-terrorist-attack/fatalities/india-jammukashmir")
table = pd.read_html(browser.page_source)[1]
table.to_excel(r"J & K Terrorism History DataBase\Fatalities\fatalities.xlsx")
while browser.execute_script('return document.readyState') != "complete":
    time.sleep(1)
    print(browser.execute_script('return document.readyState'))
    
while True:
    s = ""
    if len(str(i)) == 1:
        s = "0"+str(i)
    else:
        s = str(i)
    time.sleep(3)
    try:
        year = browser.execute_script("""return document.getElementById('ctl00_ContentPlaceHolder1_gvFatalities_ctl""" + s +  """_lbtnYear').text;""")
    except:
        break
    if "*" in year:
        year = year[0:-1]
    try: 
        browser.execute_script("""document.getElementById('ctl00_ContentPlaceHolder1_gvFatalities_ctl""" + s +  """_lbtnYear').click();""")
    except:
        break
    time.sleep(3)
    while browser.execute_script('return document.readyState') != "complete":
        time.sleep(1)
        print(browser.execute_script('return document.readyState'))
    table = pd.read_html(browser.page_source)[1]
    try:
        table.to_excel(r"J & K Terrorism History DataBase\Fatalities\ " + str(year) + ".xlsx")
        print("Excel file has been created successfully!")
    except:
        print("ERROR")
    browser.get("https://www.satp.org/datasheet-terrorist-attack/fatalities/india-jammukashmir")
    i += 1


