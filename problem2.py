# text to voice basic

# import pyttsx3

# engine = pyttsx3.init()

# text = input("Enter something: ")  # Get text from user
# engine.say(text)                   # Queue the text to be spoken
# engine.runAndWait()                # Speak it out loud


# -----------------------------------------------



import pyttsx3

engine = pyttsx3.init()

# 🔹 Set slower speaking rate
rate = engine.getProperty('rate')      # Get current rate (default ~200)
engine.setProperty('rate', 125)        # Set slower rate (try 125 or lower)

# 🔹 Speak user input
text = input("Enter something: ")
engine.say(text)
engine.runAndWait()
