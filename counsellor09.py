# We're going to choose a response at random.  To do this, we need to import
# the *random* module.  Imports almost always come at the top of a script.
import random

name = raw_input("What is your name? ")
print "Hello", name

# We can spread lists out over several lines.
words_of_comfort = [
    "Would you like a cup of tea?",
    "How about a cup of tea?",
    "Have you ever thought about drinking more tea?"
]

# We choose some advice at random.
advice = random.choice(words_of_comfort)

mood = raw_input("How are you today? ")

print "That's nice dear."
print advice

# Question: What happens if we leave out the comma at the end of line 13?
# Question: What happens if we put a comma at the end of line 15?
