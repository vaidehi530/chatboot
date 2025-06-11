import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I can't reach the server right now.")
            return ""
        except sr.WaitTimeoutError:
            speak("You didn’t say anything.")
            return ""


def chatbot_reply(command):
    if "hello" in command:
        return "Hi there! How can I help you?"

    elif "your name" in command:
        return "I am your voice chatbot assistant."

    elif "how are you" in command:
        return "I'm just a bot, but I'm doing great!"
    
    elif "open google" in command:
      webbrowser.open("https://www.google.com")
      return "opening google..."


    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {time}"

    elif "play music" in command:
        music_dir = "C:/Users/YourUsername/Music"  # 🔁 Replace with your actual music folder path
        try:
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            return "Playing music..."
        except:
            return "Couldn't find music folder."

    elif "joke" in command:
        return "Why did the computer go to therapy? Because it had too many bytes of trauma!"

    elif "note" in command:
        speak("What should I write?")
        note = listen()
        with open("note.txt", "a") as f:
            f.write(note + "\n")
        return "Note saved successfully."
    
    elif "open calculator" in command:
       os.system("calc")
       return "opening calculator "

    elif "open paint" in command:
       os.system("mspaint")
       return "opening mspaint "
 

    elif "bye" in command or "exit" in command:
        return "Goodbye! Have a nice day."

    else:
        return "I'm not sure how to respond to that."

# Main Chat Loop
speak("Hi, I am your voice assistant. You can start talking now.")

while True:
    user_input = listen()
    if "bye" in user_input or "exit" in user_input:
        speak("Goodbye!")
        break
    response = chatbot_reply(user_input)
    speak(response)
