name = raw_input("What is your name? ")
print "Hello", name

# We can do many tests in one go.  If the first test doesn't succeed, then we
# try the second test, and so on.  *elif* is short for *else if*.
mood = raw_input("How are you today? ")
if mood == "Sad" or mood == 'sad':
    print "That's a shame.  Would you like a cup of tea?"
elif mood == "Happy" or mood == 'happy':
    print "That's nice.  Would you like a cup of tea?"
else:
    print "I don't know what that means.  Would you like a cup of tea?"

# Task: Add another *elif* branch to test whether the user is angry.
