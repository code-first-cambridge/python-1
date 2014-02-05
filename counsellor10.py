name = raw_input("What is your name? ")
print "Hello", name

mood = raw_input("How are you today? ")
print "That's nice dear.  Would you like a cup of tea?"

# We can open a file, which we'll later write to.  The "w" means that we're
# opening the file for writing.
f = open("database.txt", "w")

# We can easily write strings to a file.
f.write(name)
f.write(",")
f.write(mood)

# We're going to add a newline character to the end of the line.  Don't worry
# too much about this for now!
f.write("\n")

# We should close a file after we've finished with it.
f.close()

# Question: What happens if we don't include the "w" when opening the file?
