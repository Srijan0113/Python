#weather app
import requests
import json
import win32com.client as wc

city=input("Enter the name of the city  : \n ")
url=f"https://api.weatherapi.com/v1/current.json?key=YOUR-API-KEY&q={city}"

r=requests.get(url)
#print(r.text)
#print(type(r.text)) #string type 
wdic=json.loads(r.text) #convert to python dictionary from json string

speaker = wc.Dispatch("SAPI.SpVoice")
for key,value in wdic.items():
    
    text=f"{key} is {value}"
    print(text)
    #speaker.Speak(text)

keys_location=["name","region","country","lat","lon","localtime"]
keys_current=['last_updated','temp_c','feelslike_c','temp_f','humidity','condition','wind_dir','wind_kph']

print(f"---------Weather report of {city} ----------")
for key in keys_location:
    value=wdic["location"][key]
    print(f"{key.capitalize()}:{value}")
    speaker.speak(f"{key} is {value}")


for key in keys_current:
    value=wdic["current"][key]
    #condition itself is a dict -> take only "text"
    if isinstance(value,dict):
         value=value["text"]
         
    print(f"{key.capitalize()}:{value}")
    speaker.speak(f"{key} is {value}")



