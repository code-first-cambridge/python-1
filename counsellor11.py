# We can reopen the file.  This time we don't need the "w" since we're not
# writing to the file.
f = open("database.txt")

# We can read the first line in the file.
line = f.readline()

# We should close a file after we've finished with it.
f.close()

# The value of *line* is going to be something like "Peter,Happy\n".  We can
# strip the newline character, and then split this up into a list.
data = line.strip().split(",")

# The value of *data* is going to be a list like ["Peter", "Happy"].  We can
# access individual elements of a list.
name = data[0]
mood = data[1]

print "Hello", name
print "Last time I saw you, you said that you were", mood

# Question: What happens if the file doesn't exist?
# Question: What would have happened if the user's name was something like
# "Smith, J."?
# Question: What would have happened if the user had said that they were "Very
# happy, thank you for asking"?

# See http://docs.python.org/2/library/stdtypes.html#str.split for more about
# splitting strings.
