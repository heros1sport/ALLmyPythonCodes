import gtts
import os
from playsound import playsound
import webbrowser


try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import urllib
url = input()


html = """
<div class='magical'><p><div><div>something</div></div></p></div>
"""
parsed_html = BeautifulSoup(html,features = "html.parser")
Text = "" 
for i in parsed_html.find_all():
    try:
        Text += BeautifulSoup(str(i),features = "html.parser").text
    except:
        pass
print(Text)


Text = Text.split('\n')
Trimmed = []
for i in range(len(Text)):
    try:
        if len(Text[i]) > 0:
            Trimmed.append(Text[i])
    except:
        pass


final = ""
for i in Trimmed:
    final += i + "\n"
    


for i in Trimmed:
    for j in i.split("."):
        print(j)
        g = gtts.gTTS(j)
        

        g.save("YourFile.mp3")
        
        
        
        playsound("YourFile.mp3")
            
        os.remove("YourFile.mp3")



