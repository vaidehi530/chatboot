import pyttsx3

def list_voices(engine):
    voices = engine.getProperty('voices')
    print("Available voices:\n")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} - {voice.id}")
    return voices

def choose_voice(engine, voices):
    while True:
        try:
            choice = int(input("\nEnter the number of the voice you want to try: "))
            if 0 <= choice < len(voices):
                engine.setProperty('voice', voices[choice].id)
                engine.say("Hello! This is the voice you selected.")
                engine.runAndWait()
                print(f"You heard voice: {voices[choice].name}")
                break
            else:
                print(f"Please enter a number between 0 and {len(voices) - 1}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    engine = pyttsx3.init()
    voices = list_voices(engine)
    choose_voice(engine, voices)

if __name__ == "__main__":
    main()
