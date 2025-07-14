import random

# Some user inputs and bot replies
pairs = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing great!"],
    "bye": ["Goodbye!", "See you later!"],
}

def get_reply(user_input):
    user_input = user_input.lower()
    if user_input in pairs:
        return random.choice(pairs[user_input])
    else:
        return "Sorry, I don't understand that."

# Chat loop
print("AI Agent: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("AI Agent: Bye!")
        break
    response = get_reply(user)
    print("AI Agent:", response)
