import pyttsx3
import os,subprocess,time
import speech_recognition as sr  
import json
import requests
import webbrowser
import psutil
import tkinter
import vlc
import cv2
import xlwt

from weather import Weather, Unit
from gi.repository import Gdk
from datetime import datetime
from subprocess import call
from tkinter import *

r=sr.Recognizer()
engine=pyttsx3.init()



if(datetime.now().strftime('%H')>'11' and datetime.now().strftime('%H')<'17'):
    print("Good afternoon")
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say("Good afternoon")
    engine.runAndWait()
elif(datetime.now().strftime('%H')>'17' and datetime.now().strftime('%H')<'23'):
    print("Good evening")
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say("Good evening")
    engine.runAndWait()
else:
    print("Good morning")
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say("Good morning")
    engine.runAndWait()

##print("To access the bot please provide some necessary information")
##name1=input('For security pupose,enter your name:')
##relation=input('Relationship with Divyansh:')
##p1=xlwt.easyxf("Font:name Times New Roman,color-index red,bold on",num_format_str="#,##0.00");
##wb=xlwt.Workbook()
##ws=wb.add_sheet("sheet1",cell_overwrite_ok=True)
##ws.write(0,0,"name",p1)
##ws.write(0,1,"relationship",p1)
##ws.write(1,0,name1,p1)
##ws.write(1,1,relation,p1)
##wb.save("bot_database.xls")
##
##camera=cv2.VideoCapture(0)
##ret,img=camera.read()
##print(ret)
##loc='abc.jpg'
##cv2.imwrite(loc,img)
##del(camera)
##face_cascade=cv2.CascadeClassifier('/usr/local/lib/python3.5/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
##img=cv2.imread('abc.jpg')
##gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##faces=face_cascade.detectMultiScale(gray,1.3,9,minSize=(80,80))
##for (x,y,w,h) in faces:
##    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
##cv2.namedWindow('my_image',cv2.WINDOW_NORMAL)
##cv2.resizeWindow('my_image',640,480)
####cv2.imshow('my_image',img)
####cv2.waitKey(0)
####cv2.destroyAllWindows()gg
##engine.say("Sorry ! but we have captured your picture")
##engine.runAndWait()
##print('Sorry ! but we have captured your picture')

    
print("Adjusting, please wait....")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    while(1):
        print("Speak:")
        audio = r.listen(source)                      
        try:
        
            data=r.recognize_google(audio)
            print("You said " + data)             
            rate=engine.getProperty('rate')
            engine.setProperty('rate',rate-30)
            engine.say(data)
            engine.runAndWait()
            
            if 'calculator' in data:
                print("Opening Calculator")
                engine.say("Searching for: Calculator")
                subprocess.Popen('gnome-calculator')
                
            elif 'spreadsheet' in data:
                print("Opening Spreadsheet")
                engine.say("Searching for: LibreOffice")
                subprocess.Popen('libreoffice')
                
            elif 'calendar' in data:
                print("Opening Calendar")
                engine.say("Searching for: Calendar")
                subprocess.Popen('gnome-calendar')
                
                
            elif 'g edit' in data:
                print("Opening Text Editor-G edit")
                engine.say("Searching for: gedit")
                subprocess.Popen('gedit')
                
            elif 'search' in data:
                splitdata=data.split()
                words=['search']
                resultwords=[word for word in splitdata if word.lower() not in words]
                result=' '.join(resultwords)
                print("Searching for:" + result)
                engine.say("Searching for:" + result)
                engine.runAndWait()
                webbrowser.open('https://www.google.co.in/search?q=' + result)
                
            elif 'shutdown' in data: 
                r1=sr.Recognizer()
                with sr.Microphone() as source:
                    r1.adjust_for_ambient_noise(source)
                    while(1):
                        print("Are you sure")
                        audio=r1.listen(source)
                        try:
                            data1=r1.recognize_google(audio)
                            if 'yes' in data1:
                                print("Shutting Down")
                                engine.say("Shutting Down")
                                cmdCommand = "shutdown -h now"
                                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                            else:
                                print("Shutting Down")
                                engine.say("Try Again")
                        except sr.UnknownValueError:
                            print("Could not understand audio")   
                        except sr.RequestError as e:
                            print("Could not request results; {0}".format(e))
            
            elif 'sound' in data:
                splitdata=data.split()
                words=['change','sound','to','system','decrease','increase']
                resultwords=[word for word in splitdata if word.lower() not in words]
                result=' '.join(resultwords)
                print(result)
                call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
                valid = False
                while not valid:
                    volume=result
                    try:
                        volume=int(volume)
                        if(volume <= 100) and (volume >= 0):
                            call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
                            valid = True
                    except ValueError:
                        pass
                print(volume)
                
            elif 'brightness' in data:
                splitdata=data.split()
                words=['change','brightness','to','system','decrease','increase','the']
                resultwords=[word for word in splitdata if word.lower() not in words]
                result=' '.join(resultwords)
                os.system('xbacklight -set ' + str(result))

            elif 'picture' in data:
                print("Capturing Image...")
                engine.say("Capturing Image")
                engine.runAndWait()
                camera=cv2.VideoCapture(0)
                ret,ing=camera.read()
                print(ret)
                loc="abc.jpg"
                cv2.imwrite(loc,ing)
                del(camera)
                
                
            elif 'weather' in data:
                splitdata=data.split()
                words=['tell','give','me','provide','the','of','weather','what','is','temperature']
                resultwords=[word for word in splitdata if word.lower() not in words]
                result=' '.join(resultwords)
                weather = Weather(unit=Unit.CELSIUS)
                location = weather.lookup_by_location('result')
                forecasts = location.forecast
                for forecast in forecasts:
                    print("Weather forecast:" + str(forecast.text))
                    print(forecast.date)
                    print("Highest temperature:" + str(forecast.high))
                    print("Lowest temperature:" + str(forecast.low))
                    
            elif 'screenshot' in data:
                window = Gdk.get_default_root_window()
                x, y, width, height = window.get_geometry()
                print("The size of the root window is {} x {}".format(width, height))
                pb = Gdk.pixbuf_get_from_window(window, x, y, width, height)
                if pb:
                    pb.savev("screenshot.png", "png", (), ())
                    print("Screenshot saved to ML Folder on Desktop")
                else:
                    print("Unable to get the screenshot.")
                    
            elif 'call' in data:
                splitdata=data.split()
                words=['call','me']
                resultwords=[word for word in splitdata if word.lower() not in words]
                result=' '.join(resultwords)
                engine.say("hello" + result)
                engine.runAndWait()
                print("from now onwards i will call you" + result)
                
            elif 'cd rom' in data:
                print("opening cd rom")
                try:
                    os.system("eject cdrom")
                    time.sleep(5)
                except:
                    print("error")

            elif 'battery' in data:
                rate=engine.getProperty('rate')
                engine.setProperty('rate',rate-30)
                engine.say("Gathering Battery Status")
                engine.runAndWait()
                print("Gathering Battery Status")
                print('Battery Left (in %) : '+str (psutil.sensors_battery()[0]))
                print('Seconds Left :' + str(psutil.sensors_battery()[1]))
                print('Charger Plugged :' + str(psutil.sensors_battery()[2]))

            elif 'location' in data:
                sendurl="http://api.ipstack.com/check?access_key=a9118e2a612fc25bd8962da760ea36c6&format=1"
                req=requests.get(sendurl)
                j=json.loads(req.text)
                print('Current city is:' + str(j['city']))
                print('Current IP is:' + str(j['ip']))
                print('Current state is:' + str(j['region_name']))
                print('Your Current zip:'+ str(j['zip']))
                print('Current State is: '+ str(j['location']['capital']))
                

            elif 'music' in data:
                root=Tk()
                root.grid()
                root.geometry("1000x1000+0+0")
                root.title("Music System")

                a=IntVar()
                b=IntVar()
                c=IntVar()
                d=IntVar()
                p= vlc.MediaPlayer()
                def Nucleya1():
                    global p
                    p.stop()
                    p = vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 01 Nucleya - Laung Gawacha feat. Avneet Khurmi.mp3")
                    p.play()
                    print("Playing Laung Gwacha...")
                def Nucleya2():
                    global p
                    p.stop()
                    p = vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 03 Jungle Raja feat. Divine & Gagan Mudgal.mp3")
                    p.play()
                    print("Playing Jungle Raja...")
                def Nucleya3():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 05 Chennai Bass feat. Siva Mani & Chinna Ponnu.mp3")
                    p.play()
                    print("Playing Chennai Bass")
                def Nucleya4():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 06 Heer feat. Shruti Pathak (Dirty Dewarist Remix).mp3")
                    p.play()
                def Nucleya5():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 07 Mumbai Dance Feat. Julius Sylvest.mp3")
                    p.play()
                def Nucleya6():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/nucleya/Nucleya - Bass Rani - 08 F-k Nucleya.mp3")
                    p.play()
                    

                def Arijit1():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/ankit/Milne Hai Mujhse Aayi [Aashiqui 2].mp3")
                    p.play()
                    print("Playing Milne he mujhse aayi...")
                def Arijit2():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/ankit/Phir Mohabbat [Murder 2].mp3")
                    p.play()
                    print("Playing Phir mohabatt karle jara...")
                def Arijit3():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/arijit/03 - A2 - Chahun Main Ya Naa .mp3")
                    p.play()
                    print("Playing Chahun main ya na...")
                def Arijit4():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/ankit/Sun Le Zara [Singham Returns].mp3")
                    p.play()
                    print("Playing Sun le zara...")


                def Atif1():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/01-Doorie(www.songs.pk).mp3")
                    p.play()
                    print("Playing Doorie, sahi jae na...")
                def Atif2():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/01 - Tu Khaas Hai - [rKmania.me].mp3")
                    p.play()
                    print("Playing Tu khass hai...")
                def Atif3():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/02-Aadat (atif).mp3")
                    p.play()
                    print("Playing Aadat...")
                def Atif4():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/02 Bakhuda Tumhi Ho [FilmiXpress.Net].mp3")
                    p.play()
                    print("Playing Bakhuda tumhi ho...")
                def Atif5():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/04 -  Tu Mohabbat Hai.mp3")
                    p.play()
                    print("Playing Tu mohabbat hai...")
                def Atif6():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/atif/[Songs.PK] F.A.L.T.U - 01 - Le Ja Tu Mujhe.mp3")
                    p.play()
                    print("Playing Le ja tu mujhe...")
                    

                def Old1():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/old/Aaj Mausam Bada Beimaan Hai.mp3")
                    p.play()
                    print("Playing Aaj mausam bada baiman hai...")
                def Old2():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/old/Bindiya chamke gi.mp3")
                    p.play()
                    print("Playing Bindiya chamkegi...")
                def Old3():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/old/Jane kyon log Mohabbat kiya karate hain.mp3")
                    p.play()
                    print("Playing Jane kyon log Mohabbat kiya karate hai...")
                def Old4():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/old/Jhoom jhoom.mp3")
                    p.play()
                    print("Playing Jhoom jhoom...")
                def Old5():
                    global p
                    p.stop()
                    p=vlc.MediaPlayer(r"/home/divyansh/Desktop/old/Mujhe peene ka shuaq.mp3")
                    p.play()
                    print("Playing Mujhe peena ka shaq nhi...")


                temp=Button(text="Atif",fg="white",bg="blue",font=30,activeforeground="red",activebackground="yellow",bd=3,relief="sunken").grid(row=1,column=1)
                temp=Button(text="Arijit",fg="white",bg="blue",font=30,activeforeground="red",activebackground="yellow",bd=3,relief="sunken").grid(row=1,column=5)
                temp=Button(text="Nucleya",fg="white",bg="blue",font=30,activeforeground="red",activebackground="yellow",bd=3,relief="sunken").grid(row=1,column=9)
                temp=Button(text="Old",fg="white",bg="blue",font=30,activeforeground="red",activebackground="yellow",bd=3,relief="sunken").grid(row=1,column=13)

                button=Radiobutton(root,text="Doorie",variable=a,value=1,command=Atif1)
                button.grid(row=2,column=1,sticky=W)
                button=Radiobutton(root,text="Tu Khaas Hai",variable=a,value=2,command=Atif2)
                button.grid(row=3,column=1,sticky=W)
                button=Radiobutton(root,text="Aadat",variable=a,value=3,command=Atif3)
                button.grid(row=4,column=1,sticky=W)
                button=Radiobutton(root,text="Bakhuda Tumhi Ho",variable=a,value=4,command=Atif4)
                button.grid(row=5,column=1,sticky=W)
                button=Radiobutton(root,text="Tu Mohabbat Hai",variable=a,value=5,command=Atif5)
                button.grid(row=6,column=1,sticky=W)
                button=Radiobutton(root,text="Le Ja Tu Mujhe",variable=a,value=6,command=Atif6)
                button.grid(row=7,column=1,sticky=W)

                button=Radiobutton(root,text="Milne He Mujhse Aayi",variable=b,value=1,command=Arijit1)
                button.grid(row=2,column=5,sticky=W)
                button=Radiobutton(root,text="Phir Mohabbat",variable=b,value=2,command=Arijit2)
                button.grid(row=3,column=5,sticky=W)
                button=Radiobutton(root,text="Chahun Main Ya Naa",variable=b,value=3,command=Arijit3)
                button.grid(row=4,column=5,sticky=W)
                button=Radiobutton(root,text="Sun Le Zara",variable=b,value=4,command=Arijit4)
                button.grid(row=5,column=5,sticky=W)

                button=Radiobutton(root,text="Laung Gawacha",variable=c,value=1,command=Nucleya1)
                button.grid(row=2,column=9,sticky=W)
                button=Radiobutton(root,text="Jungle Raja",variable=c,value=2,command=Nucleya2)
                button.grid(row=3,column=9,sticky=W)
                button=Radiobutton(root,text="Chennai Bass",variable=c,value=3,command=Nucleya3)
                button.grid(row=4,column=9,sticky=W)
                button=Radiobutton(root,text="Nucleya 1",variable=c,value=4,command=Nucleya4)
                button.grid(row=5,column=9,sticky=W)
                button=Radiobutton(root,text="Nucleya 2",variable=c,value=5,command=Nucleya5)
                button.grid(row=6,column=9,sticky=W)
                button=Radiobutton(root,text="Nucleya 3",variable=c,value=6,command=Nucleya6)
                button.grid(row=7,column=9,sticky=W)

                button=Radiobutton(root,text="Aaj Mausam Bada Baiman Hai",variable=d,value=1,command=Old1)
                button.grid(row=2,column=13,sticky=W)
                button=Radiobutton(root,text="Bindiya Chamkegi",variable=d,value=2,command=Old2)
                button.grid(row=3,column=13,sticky=W)
                button=Radiobutton(root,text="Jane Kyon Log Pyar Karte He",variable=d,value=3,command=Old3)
                button.grid(row=4,column=13,sticky=W)
                button=Radiobutton(root,text="Jhoom Jhoom",variable=d,value=4,command=Old4)
                button.grid(row=5,column=13,sticky=W)
                button=Radiobutton(root,text="Mujhe Peene Ka Shuaq",variable=d,value=5,command=Old5)
                button.grid(row=6,column=13,sticky=W)
                
   

                    
                
        except sr.UnknownValueError:
            print("Could not understand audio")   
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e)) 
            
        
        


