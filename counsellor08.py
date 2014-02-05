name = raw_input("What is your name? ")
print "Hello", name

# We can assign a list of values to a label.
bad_moods = ["Sad", "Angry", "Grumpy"]
good_moods = ["Happy", "Cheerful", "Jolly"]

mood = raw_input("How are you today? ")

# We can then test whether a string is in a list.
if mood in bad_moods:
    print "That's a shame.  Would you like a cup of tea?"
elif mood in good_moods:
    print "That's nice.  Would you like a cup of tea?"
else:
    print "I don't know what that means.  Would you like a cup of tea?"

# Question: What would happen if the same string appeared in both *bad_moods*
# and *good_moods*?
