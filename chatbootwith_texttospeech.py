import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the bot speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# The chatbot function
def chatbot():
    print("Bot: Hello! I'm ChatBot. Type 'bye' to exit.")
    speak("Hello! I'm ChatBot. Type bye to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            reply = "Hi there! How can I help you?"
        elif "how are you" in user_input:
            reply = "I'm just a program, but I'm doing great!"
        elif "your name" in user_input:
            reply = "I'm a chatbot created by you."
        elif "book" in user_input:
            reply = "Books are a great source of knowledge."
        elif "fan" in user_input:
            reply = "A fan is a device that moves air to keep things cool."
        elif "chair" in user_input :
            reply= "used to sit ."
            
        elif "bye" in user_input:
            reply = "Goodbye! Have a great day."
            print("Bot:", reply)
            speak(reply)
            break
        else:
            reply = "I'm not sure about that. Can you ask something else?"

        print("Bot:", reply)
        speak(reply)

# Run the chatbot
chatbot()
