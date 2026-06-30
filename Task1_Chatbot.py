def get_bot_response(user_input):
    #Convert the user's input to lowercase
    text = user_input.lower()

    # ---Predefined Rules using if-elif-else ---

    if "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"
    
    elif "your name" in text:
        return "I am a simple rule-based  chatbot"
    
    elif "how are you" in text: 
        return "I am just a bunch of Python code, but I'm doing great! How are you?"
    
    elif "weather" in text: 
        return "I hope it's nice outside!"
    
    elif "book" in text:
        return "Atomic Habits' is a phenomenal book if you like self-improvement."
    
    elif "bye" in text or "exit" in text:
        return "Goodbye! Have a phenomenal day!" 
    
    else:
        # The 'else' statement acts as a fallback if no others rule match
        return "I'm sorry, I don't understand that. My rules are limited. Try saying 'hello' or asking about a 'book'. "
    
 # --- Main Game/Chat Loop ---
print("Chatbot:  Hi! I am online. (Type 'bye' to exit)") 
    
while True:
     # 1. Get input from the user 
    user_message = input("You: ")

    # 2. Pass the input to our rule function
    bot_reply = get_bot_response(user_message)

    # 3. Print the bot's respone
    print("Chatbot:", bot_reply) 

    # 4. Check if the loop needs to end
    if "bye" in user_message.lower() or "exit" in user_message.lower():
        break 
