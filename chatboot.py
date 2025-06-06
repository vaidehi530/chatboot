def chatbot():
    print("Hello! I'm ChatBot. Ask me something. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great!")
        elif "your name" in user_input:
            print("Bot: I'm a chatbot created by you.")
        elif "book" in user_input:
            print("Bot: Books are a great source of knowledge. Do you like fiction or non-fiction?")
        elif "fan" in user_input:
            print("Bot: A fan is an electrical device that circulates air to cool a room.")
        elif "computer" in user_input:
            print("Bot: A computer is an electronic machine that processes data and performs tasks.")
        elif "teacher" in user_input:
            print("Bot: A teacher is someone who helps others learn new things.")
        elif "cloth" in user_input:
            print("Bot: used to cover the body .") 
        elif "home" in user_input :
            print(" Bot: home is a place whwere we can live .")
        elif "laptop" in user_input :
            print("Bot: laptop is device which works like computer with advantage that it is easy to carry .")
        elif "bed " in user_input :
            print("Bot: it is furniture used for sleeping .")
        elif "comb" in user_input :
            print(" used for grooming purpose to combing our hair .")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day.")
           
            break
        else:
            print("Bot: I'm not sure about that. Can you ask something else?")

chatbot()
