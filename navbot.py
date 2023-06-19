import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import openai
from PIL import Image, ImageTk
import tkinter as tk
import webbrowser
import sys
import time
import colorama
from colorama import Fore, Back, Style

openai.api_key = "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"
root = tk.Tk()
root.geometry("800x600")
root.title("SGGS Assistant")
listener = sr.Recognizer()

colorama.init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def rainbow_text(string):
    for i, char in enumerate(string):
        sys.stdout.write(colors[i % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(0.1)





try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


except Exception as e:
    engine = None
    print(f"Error initializing pyttsx3: {e}")


def talk(text):
    if engine:
        engine.say(text)
        engine.runAndWait()


def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=5
    )

    if response.choices[0].text:
        return response.choices[0].text.strip()
    else:
        return ""


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        rainbow_text("Listening...")
        output_label.config(text="Listening...")
        root.update()
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        output_label.config(text="Could not understand audio.")
        output_label.config(text="Could not understand audio.")
        root.update()
        print("error block 1")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        output_label.config(text="Could not request results.")
        output_label.config(text="Could not request results.")
        root.update()
        print("error block 2")
        return ""


def run_assistant():

    command = take_command()
    print(command)

    if not command:
        output_label.config(text="Could not understand audio.")
        return

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        rainbow_text("code block 1 executed ")
        output_label.config(text='Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        try:
            info = wikipedia.summary(person, 1)
            rainbow_text(info)
            talk(info)
            output_label.config(text=info)
            print("code block 2 executed ")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Error getting Wikipedia info: {e}")
            output_label.config(text="Could not get Wikipedia info.")
    elif 'direction to admin' in command or 'admin' in command or 'from gate' in command or 'to admin' in command:
        direction_ad = "From the main entrance, go straight for 200 meters, then walking through the left-hand side stairs on the second floor, your destination is 10 m from right"
        rainbow_text(direction_ad)
        talk(direction_ad)
        output_label.config(text=direction_ad)
        print("code block 3 executed ")
    elif'website' in command:
        talk("Opening the website in browser")
        url=f"https://www.sggs.ac.in/"
        output_label.config(text="Opening Google...")
        root.update()
        def open_url():
            webbrowser.open(url)
        open_url()
        root.mainloop()
        print("code block 4 executed ")
    elif 'location' in command:
        talk("Opening the location in browser")
        latitude = 19.1121525595
        longitude = 77.2931926029
        url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
        output_label.config(text="Opening Google Maps...")
        root.update()
        print("code block 5 executed ")
        def open_url():
            webbrowser.open(url)

        open_url()
        root.mainloop()
    elif 'direction to admin' in command or 'admin' in command or 'from gate' in command or 'to admin' in command:
        direction_ad = "From the main entrance, go straight for 200 meters, then walking through the left-hand side stairs on the second floor, your destination is 10 m from right"
        rainbow_text(direction_ad)
        talk(direction_ad)
        output_label.config(text=direction_ad)
        print("code block 6 executed ")


    elif 'girls' in command or ' to admin' in command or 'from admin ' in command or 'to girls hostel' in command:
        direction_GH = 'From admin go straight few step and then turn left side ........and walk staright for atleast 160 meters and then turn right ..... than u reach girl hostel their destinations'
        rainbow_text(direction_GH)
        talk(direction_GH)
        output_label.config(text=direction_GH)
        print("code block 7 executed ")


    elif 'canteen' in command or 'canteen' in command or 'lunch' in command or 'to canteen' in command:
        direction_can = 'From admin go straight few step and then turn left side.....and walk staright for atleast 50 meters ..........and then turn left and walk 100 meters......u will reach to ur destination'
        rainbow_text(direction_can)
        talk(direction_can)
        output_label.config(text=direction_can)
        print("code block 8 executed ")


    elif 'boys' in command or ' sahaydri hostel' in command or 'nandgiri hostel' in command or 'from admin ' in command or 'boys hostel' in command:
        direction_bh = 'From admin go straight few step and then turn left side........and walk staright for atleast 50 meters ..... and then turn left and walk 350 meters and ;;;;;;;;;again turn left and walk for 100 meters........... here is ur destinations boys hostel'
        rainbow_text(direction_bh)
        talk(direction_bh)
        output_label.config(text=direction_bh)
        print("code block 9 executed ")


    elif 'atm' in command or 'atm from admin' in command or 'atm' in command or 'money' in command:
        direction_at = 'From admin go straight few step and....... then turn left side  and walk ..... staright for atleast 50 meters  .....and then turn left and walk 70 meters.... on your right hand side u will see the board of ATM........ finally u reached to ur destinations '
        rainbow_text(direction_at)
        talk(direction_at)
        output_label.config(text=direction_at)
        print("code block 10 executed ")


    elif 'lawn' in command:
        direction_la = 'From admin when you are coming out the left side you will see a lawn ....that is director lawn'
        rainbow_text(direction_la)
        talk(direction_la)
        output_label.config(text=direction_la)
        print("code block 11 executed ")

    elif 'hostel' in command or 'hostel office' in command or ' from admin ' in command:
        direction_ho = 'From admin go straight few step and then turn left side .... and walk ........staright for atleast 50 meters  and then turn left and .......walk 350 meters and again turn left .........you will see the board of hostel office'
        rainbow_text(direction_ho)
        talk(direction_ho)
        output_label.config(text=direction_ho)
        print("code block 12 executed ")

    elif 'director sir cabin' in command or 'director' in command or 'director cabin' in command or 'director office' in command:
        direction_do = 'when u enter admin building from left side step go to first floor and than again turn left and walk straight...... you will get the director sir cabin.......... with director name in front of his cabin '
        rainbow_text(direction_do)
        talk(direction_do)
        output_label.config(text=direction_do)
        print("code block 13 executed ")


    elif 'dean' in command or 'academic' in command or 'acadmeic dean office ' in command:
        direction_ad = 'when u enter admin building from left side step go to first floor and than again turn left and walk straight.......again move left.... u will see the board of acadmeic dean...... finally u reached to ur destinations '
        rainbow_text(direction_ad)
        talk(direction_ad)
        output_label.config(text=direction_do)
        print("code block 14 executed ")


    elif 'ground' in command or 'sport' in command or 'from admin to ground ' in command or 'arena' in command:
        direction_gd = 'From admin go straight few step and then turn left side  and walk staright for atleast 50 meters and then turn left and walk 350 meters......and again turn left and walk for 200 meters.....u will see ground... enjoy your day with different sports  '
        rainbow_text(direction_gd)
        talk(direction_gd)
        output_label.config(text=direction_gd)
        print("code block 15 executed ")



    elif 'parking' in command or 'vehicle'  in command or 'area ' in command:
        direction_gk = 'when you are entering the college the left hand side is the parking area of the college...... u will see the parking area ....... finally u reach to your destinations'
        rainbow_text(direction_gk)
        talk(direction_gk)
        output_label.config(text=direction_gk)
        print("code block 16 executed ")


    elif 'library' in command or 'college' in command or 'central' in command or 'books' in command:
        direction_lb = 'when u enter admin building...... from main door turn right side and walk few steps...... you will get the door open it and enter into library...... finally u reached to ur destinations '
        rainbow_text(direction_lb)
        talk(direction_lb)
        output_label.config(text=direction_lb)
        print("code block 17 executed ")

    elif 'account' in command  or 'section' in command or 'fees' in command:
        direction_ac = 'when u enter admin building from main door.........turn left side and walk few steps...... you will get the board account section ......thats your destination'
        rainbow_text(direction_ac)
        talk(direction_ac)
        output_label.config(text=direction_ac)
        print("code block 18 executed ")


    elif 'training' in command or 'placment' in command or  'office' in command or 'director' in command:
        direction_lbb = 'when u enter admin building.......... from main door turn left side and walk few steps...... you will get the office......with Ravinder Joshi sir cabin'
        rainbow_text(direction_lbb)
        talk(direction_lbb)
        output_label.config(text=direction_lbb)
        print("code block 19 executed ")


    elif 'ccf ' in command or 'common' in command or  'computer'  in command or 'computer lab' in command:
        direction_cf = 'when u enter admin building........ from main door turn left side and walk few steps...... ccf lab will be their........ finally u reached to ur destinations'
        rainbow_text(direction_cf)
        talk(direction_cf)
        output_label.config(text=direction_cf)
        print("code block 20 executed ")


    elif 'reading' in command or 'hall' in command or 'study' in command or 'reading hall' in command:
        direction_rd = 'when u enter admin building from right side step go to first floor and..... than again turn right and walk straight...... you will enter into the reading hall'
        rainbow_text(direction_rd)
        talk(direction_rd)
        output_label.config(text=direction_rd)
        print("code block 21 executed ")


    elif 'coe' in command or 'exam' in command or 'controller' in command or 'examination' in command:
        direction_ex = 'when u enter admin building..... from left side step go to second floor ......and than again turn left and walk straight...... u will see the a door ..... that is exam section of college ......... finally u reached to ur destinations '
        rainbow_text(direction_ex)
        talk(direction_ex)
        output_label.config(text=direction_ex)
        print("code block 22 executed ")


    elif 'dean office' in command or 'maths' in command or 'math' in command or 'mathematics'in command or 'club' in command:
        direction_sd = 'when u enter admin building ....from left side step go to second floor..... and than again turn left.....and walk straight on right hand side ..... its the office of student dean.......Dr. Arunkumar Patil sir ......our student dean '
        rainbow_text(direction_sd)
        talk(direction_sd)
        output_label.config(text=direction_sd)
        print("code block 23 executed ")


    elif 'physicslab' in command or 'lab' in command or 'physics' or 'laborotary' in command:
        direction_sde = 'when u enter admin building from left side...... step go to second floor and than again turn left and walk straight...... on left hand side ..... you will the see the board of physics lab........... finally u reached to ur destinations '
        rainbow_text(direction_sde)
        talk(direction_sde)
        output_label.config(text=direction_sde)
        print("code block 24 executed ")


    elif 'student section' in command or 'sochalarship' in command:
        direction_ss = 'when u enter admin building .........from left side step go to second floor and than go staright ........ you will see the board of........student section'
        rainbow_text(direction_ss)
        talk(direction_ss)
        output_label.config(text=direction_ss)
        print("code block 25 executed ")


    else:
        talk('Please say the command again')
        output_label.config(text='Please say the command again')


input_label = tk.Label(root, text="Speak command:")
input_label.pack()

output_label = tk.Label(root, text="")
output_label.pack()

image = Image.open("C:/Users/Abhishek/PycharmProjects/pythonProject16/sggs.90a689c573b139b861f6.png")
image = image.resize((150, 150), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack()

engine.runAndWait()
talk("Hi, I am sggs assistant. You can ask me about directions or other information about the campus. What can I help you with?")


def button_pressed():
    run_assistant()

button = tk.Button(root, text="Run Assistant", command=button_pressed)
button.pack()

root.mainloop()
