name = raw_input("What is your name? ")
print "Hello", name

bad_moods = ["Sad", "Angry", "Grumpy"]
good_moods = ["Happy", "Cheerful", "Jolly"]

mood = raw_input("How are you today? ")

# We can test whether a string is longer than a certain length.
if len(mood) > 10:
    print "You're talkative today.  Would you like a cup of tea?"
else:
    print "You're very quiet today.  How about a nice cup of tea?"

# Task: Add another *elif* branch to test whether the user's response has
# fewer than five characters.
