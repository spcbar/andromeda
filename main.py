import speech_recognition as sr
from gtts import gTTS
import os
import random
import re
import requests
from pygame import mixer

r = sr.Recognizer()
m = sr.Microphone()

try:
    myobj = gTTS(text="Hello my name is Andromeda, I am open for your requests!", lang="en", slow=False)
    rnd = random.choice("abcd352435324kjdfsighjiosfhoi3434590uf0909098cxv90cvxbkljn!@#e")
    myobj.save(rnd + "welcome.mp3")
    os.system("cd /home/pi/final/hue-cli/ && /home/pi/final/hue-cli/bin/hue.sh hue 53356")
    os.system("ffplay " + rnd + "welcome.mp3 -nodisp -autoexit >/dev/null 2>&1")
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        requests.get("http://10.0.0.149:9080/api.php?action=brightness&value=240")
        try:
            value = r.recognize_google(audio)

            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))

            requests.get("http://10.0.0.149:9080/api.php?action=brightness&value=30")
            rndt = random.choice("abcd4iouth34gh8re9shguigerbhgiufdsbhguib34uithdafioundjzifngiudfse")

            if re.search(".*(rocket|Rocket).*", value):
                myobj = gTTS(text="Yes Sir!", lang="en", slow=False)
                myobj.save(rndt + "welcomexx.mp3")

                mixer.init()
                mixer.music.load(rndt + "welcomexx.mp3")
                mixer.music.play()

                requests.get("http://10.0.0.149:9080/api.php?action=brightness&value=120")
                requests.get("http://10.0.0.149:9080/api.php?action=brightness&value=200")
                os.system("cd /home/pi/final/hue-cli/ && /home/pi/final/hue-cli/bin/hue.sh hue 12")
                os.system("cd /home/pi/final/hue-cli/ && /home/pi/final/hue-cli/bin/hue.sh sat 255")
            elif re.search(".*(satellite|Satellite).*", value):
                sat = requests.get("http://spacebar.hurma.tv/satellites")
                jsonSat = sat.json()

                myobj = gTTS(text="Captain, you are near " + jsonSat['name'] + ". You will see that for " + jsonSat['duration'] + " seconds" , lang="en", slow=False)
                myobj.save(rndt + "welcomexx.mp3")

                mixer.init()
                mixer.music.load(rndt + "welcomexx.mp3")
                mixer.music.play()
            elif re.search(".*(thank).*", value):
                myobj = gTTS(text="Thank you for your attention captain! I hope that you liked our space journey!", lang="en", slow=False)
                myobj.save(rndt + "welcomexx.mp3")

                mixer.init()
                mixer.music.load(rndt + "welcomexx.mp3")
                mixer.music.play()
            else:
                rndt = random.choice("abcd4iouth34gh8re9shguigerbhgiufdsbhguib34uithdafioundjzifngiudfse")
                myobj = gTTS(text="I dont understand your query mr. captain!", lang="en", slow=False)
                myobj.save(rndt + "welcomexx.mp3")

                mixer.init()
                mixer.music.load(rndt + "welcomexx.mp3")
                mixer.music.play()

                #os.system("ffplay " + rndt + "welcomexx.mp3 -nodisp -autoexit >/dev/null 2>&1")

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass