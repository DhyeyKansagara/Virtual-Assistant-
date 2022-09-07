import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # This line adds female voice with indian accent. had to add the indian(english) voice to microsoft, export it from registry detector and modify the file by opening it with text editor.

engine.say("Kem chhe party? patel here")
engine.say("What can I do for you?")
engine.runAndWait()

def narrate(text):
    """This function narrates the commands that was taken."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """This functions takes commands"""
    try:
        """This blocks uses mic to catch audio and then passes in speech recognizer and then is converted to text. """
        with sr.Microphone() as audioSource:
            print("listening...")
            voice = listener.listen(audioSource)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if "patel" in command:
            command = command.replace('patel', '')
            print('User Command: ' + command)

    except:
        pass
    return command

def run_patel():
    """invokes patel and takes command, identifies specific words and makes patel do things"""
    command = take_command()

    """Plays song or things on youtube"""
    if 'play' and 'on youtube' in command:
        song = command.replace('play', '').replace('on youtube', '')
        narrate('playing' + song)
        pywhatkit.playonyt(song)
    elif 'what' and 'time' in command: # shares the current time in 24hr format
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        narrate('Current time is ' + time)
    elif 'tell me about' in command: # finds the information from wikipedia
        person = command.replace('tell me about ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        narrate(info)
    elif 'talk dirty to me' in command: # says a dirty witty line
        narrate('The toilet needs to be flushed, you pig')
    elif 'joke' or 'jokes' in command: # tells a joke
        joke = pyjokes.get_joke()
        print(joke)
        narrate(joke)
    else:
        narrate('hein? what?')

while(True):
    run_patel()