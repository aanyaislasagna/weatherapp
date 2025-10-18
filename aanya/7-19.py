import tkinter as tk
import requests
from PIL import Image, ImageTk
API_KEY = 'eedee0de9c6b2decd2b2c7912625a6b0'
home = tk.Tk()
home.configure(bg = "lightskyblue")
#img = Image.open("rainy.png")
img1 = ImageTk.PhotoImage(Image.open("cloudy1.png").resize((70,70)))
img2 = ImageTk.PhotoImage(Image.open("partlycloudy1.png"))
img3 = ImageTk.PhotoImage(Image.open("rain1.png"))
img4 = ImageTk.PhotoImage(Image.open("snow1.jpg"))
img5 = ImageTk.PhotoImage(Image.open("sunny1.png"))

#photos might have more issues
#photo = tk.PhotoImage(img)
# photo1 = tk.PhotoImage(img1)
# photo2 = tk.PhotoImage(img2)
# photo3 = tk.PhotoImage(img3)
# photo4 = tk.PhotoImage(img4)
# photo5 = tk.PhotoImage(img5)

homepage = tk.Frame(home, bg= "lightskyblue")
# sanjose = tk.Frame(home, bg = "lightskyblue")
# cupertino = tk.Frame(home, bg = "lightskyblue")


dict = {"cloudy": img1, "partly cloudy": img2, "rain": img3, "snow": img4, "sunny": img5, "clear sky": img5, "broken clouds": img1, "overcast clouds": img1}
homepage.pack(fill = "both", expand = True)

home.title("fun app")
home.geometry("300x400")

# sanjose.pack(fill = "both", expand = True)
# cupertino.pack(fill = "both",expand = True)

def funct():
    message1.config(text = "Weather: San Jose")
    homepage.pack_forget()
    #sanjose.pack(fill = "both", expand = True)
    message1.pack(pady = 10)
def funct1():
    message1.config(text = "Weather: Cupertino")
def getweather():
    city = text_entry.get()
    if city == "":
        message1.config(text = "This city is invalid!")
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(link).json()
        if data.get("cod") != 200:
            message1.config(text="City not found.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        message1.config(text=f"{temp}°C\n{desc.capitalize()}\nHumidity: {humidity}%")
        
        print("I MADE IT HERE")
        print(desc)
        label = tk.Label(home, image = dict[desc] ) #IMPORTANT
        label.pack(pady = 5)
        print('heyy')
        
    except Exception as e:
        message1.config(text="Error getting weather.")
        
def sanjose():
    city = "San Jose"
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(link).json()
        if data.get("cod") != 200:
            message1.config(text="City not found.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        message1.config(text=f"{temp}°C\n{desc.capitalize()}\nHumidity: {humidity}%")
        
        print("I MADE IT HERE")
        print(desc)
        label = tk.Label(home, image = dict[desc] ) #IMPORTANT
        label.pack(pady = 5)
        print('heyy')
        
    except Exception as e:
        message1.config(text="Error getting weather.")
        
def cupertino():
    city = "Cupertino"
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(link).json()
        if data.get("cod") != 200:
            message1.config(text="City not found.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        message1.config(text=f"{temp}°C\n{desc.capitalize()}\nHumidity: {humidity}%")
        
        print("I MADE IT HERE")
        print(desc)
        label = tk.Label(home, image = dict[desc] ) #IMPORTANT
        label.pack(pady = 5)
        print('heyy')
        
    except Exception as e:
        message1.config(text="Error getting weather.")
def sf():
    city = "San Francisco"
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        data = requests.get(link).json()
        if data.get("cod") != 200:
            message1.config(text="City not found.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        message1.config(text=f"{temp}°C\n{desc.capitalize()}\nHumidity: {humidity}%")
        
        print("I MADE IT HERE")
        print(desc)
        label = tk.Label(home, image = dict[desc] ) #IMPORTANT
        label.pack(pady = 5)
        print('heyy')
        
    except Exception as e:
        message1.config(text="Error getting weather.")
  
button = tk.Button(homepage,text = "San Jose", command = sanjose, bg = "lightpink")
button.pack(pady = 10)
button1 = tk.Button(homepage,text = "Cupertino", command = cupertino, bg = "lightpink")
button1.pack(pady = 10)
button3 = tk.Button(homepage, text = "San Francisco", command = sf, bg = "lightpink")
button3.pack(pady = 10)

message1 = tk.Label(homepage, text = "welcome: choose a city", bg = "lightpink")
message1.pack(pady=10)

text_entry = tk.Entry(homepage, text = "City: ")
text_entry.pack(pady = 10)   
button2 = tk.Button(homepage, text="Go", command = getweather)
button2.pack(pady = 10)





home.mainloop()