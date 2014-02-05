f = open("database.txt")
dataset = []
for line in f.readlines():
    data = line.strip().split(",")
    dataset.append(data)
f.close()

name = raw_input("What is your name? ")
print "Hello", name

seen_before = False

for data in dataset:
    if data[0] == name:
        seen_before = True
        mood = data[1]

if seen_before:
    print "Last time I saw you, you said you were", mood
else:
    print "Pleased to meet you"

mood = raw_input("How are you today? ")
print "That's nice dear.  Would you like a cup of tea?"

# Task: Update this program so that it either adds the new user to the
# database, or updates the existing user's mood.

# Task: If we find the user's name in the dataset straightaway, it's wasteful
# to iterate over every other element in the dataset.  Investigate the *break*
# keyword to improve the situation.
