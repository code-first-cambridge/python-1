name = raw_input("What is your name? ")
print "Hello", name

# We can test whether a string has one of many values like this.
mood = raw_input("How are you today? ")
if mood == "Sad" or mood == 'sad':
    print "That's a shame.  Would you like a cup of tea?"

# Question: What would happen if we changed the *or* to *and* in line 6?
