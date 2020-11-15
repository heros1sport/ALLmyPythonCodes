import time
import gtts
import webbrowser
from playsound import playsound
import pyaudio
import wave
import speech_recognition as sr 
import urllib.request
import smtplib
import os
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def recognize():
    r = sr.Recognizer()

    audio = sr.AudioFile("output.wav")

    with audio as source:
        aud = r.record(source)

    return r.recognize_google(aud)

    os.remove("output.wav")



















def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def speak(text):
    os.remove("HELO.mp3")
    fo = gtts.gTTS(text)
    fo.save("HELO.mp3")

    playsound("HELO.mp3")
    


while True:

    record()
    try:
        words = recognize()
    except:
        
        input("Press Enter to start recording again, if not speaking")
        record()
        words = recognize()

    print("You said : "+ words)
    if True:
        if words == "weather":
            webURL = urllib.request.urlopen('https://www.bbc.com/weather/1261481')
            html = webURL.read().decode()
            parsed_html = BeautifulSoup(html,features = "html.parser")
            celsuis = parsed_html.body.find('span', attrs={'class':'wr-value--temperature--c'}).text
            word = parsed_html.body.find('div', attrs={'class':'wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque'}).text
            print("Weather outside is "+celsuis+" degrees")
            speak("Weather outside is "+ celsuis)
            print(word + " will be experienced outside")            
            speak(word + " will be experienced outside")
        if words == "open a new tab in Chrome":
            webbrowser.open('https://www.google.com')
        try:
            if words.split(' ')[0] + " " + words.split(' ')[1] == "search YouTube":
        
                query = words.split(' ')
                the_query = ""
                for i in query[2:]:
                    the_query += i + "+"
                q = ""
                for i in query[2:]:
                    q += i+ " "
                speak("Searching on youtube "+ q)
                link = "https://www.youtube.com/results?search_query="+the_query[:-1]
                print(link)
                webbrowser.open(link)
                continue
        except:
            pass

        if words.split(' ')[0] == "search":
        
            query = words.split(' ')
            the_query = ""
            for i in query[1:]:
                the_query += i+ "+"
            q = ""
            for i in query[1:]:
                q += i+ " "


            speak("Searching "+ q)
        
        
            link = "https://www.google.com/search?q="+the_query[:-1]+"&rlz=1C1CHBD_enIN912IN912&oq=how+to+make+a+cake&aqs=chrome..69i57j0l7.3038j0j7&sourceid=chrome&ie=UTF-8"
            print(link)
            webbrowser.open(link)
        if words == "send mail":
            print("First please login to your account")
            email = input("email : ")

            password = input("password : ")

            import smtplib, ssl

            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Try to log in to server and send email
            try:
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(email, password)
                print("Logged in succesfully!")
                receiver = input("whom would you like to send a mail to (email id) : ")
                body = input("Your Message Here : ")
                server.sendmail(email, receiver, body)
            except Exception as e:
                print("Oops, couldn't login")
            finally:
                server.quit()
        if words == "Python shell":
            speak("opening python shell")
            os.startfile("IDLE (Python 3.7 32-bit)")
        if words.split()[0] == "start":
            speak("Enter the name of the file you want to open")
            os.startfile(input("filename : "))
            
        if words == "hello Jarvis":
            speak("Hello, Shaurya")
        if words == "how are you Jarvis":
            speak("I am fine as always, my friend")
        if words == "PIP install":
            fgh = input("Name of the module : ")
            os.system("pip install "+fgh)
   

    



   





