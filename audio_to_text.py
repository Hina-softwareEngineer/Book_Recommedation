#!/usr/bin/env python
# coding: utf-8

# In[5]:


import urllib
import speech_recognition as sr

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def speech():
    if connected():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening")
    # read the audio data from the default microphone
            audio_data = r.listen(source,timeout=5)
            print("Time over")
            print("Recognizing...")
    # convert speech to text
            text = r.recognize_google(audio_data ,language='en-UK', show_all=True)
            try:
                print("You said:" )
                if (len(text)>0):
                    print(text["alternative"][0]["transcript"])
                    print(text)
                else:
                    print("\tNothing")
            except LookupError:
                print("Could not Understand Value")

            except sr.UnknownValueError:
                print("Voice Recognition could not understand audio")

            except sr.RequestError as e:
                print("Voice Recognition could not request results ; {0}".format(e))
    else:
        print("NO Internet Connection. \nCheck your Internet Connection")
    print("Completed")
    


# In[ ]:





# In[ ]:




