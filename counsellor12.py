# We want to record all the interactions we've had with users, one per line in
# our file.  We can then load the file's contents into a list of lists.
f = open("database.txt")

# We start with an empty list.
dataset = []

# We then iterate over every line in the file.
for line in f.readlines():
    # The following code block gets executed once for every line in the file.
    # For each line in the file, the value of *line* is going to be something
    # like "Peter,Happy\n".
    data = line.strip().split(",")
    dataset.append(data)

f.close()

print "I've met", len(dataset), "people"

# We can print an empty line
print

for data in dataset:
    # The following code block gets executed once for every item in *dataset*.
    # For each iteration, *data* is going to be a list with two elements, like
    # ["Peter", "Happy"].
    name, mood = data
    print name, "was", mood

print

name = raw_input("What is your name? ")
print "Hello", name

mood = raw_input("How are you today? ")
print "That's nice dear.  Would you like a cup of tea?"

# We can add the new data to the dataset.
new_data = [name, mood]
dataset.append(new_data)

# We can write the updated dataset back to the file.
f = open("database.txt", "w")

for data in dataset:
    f.write(data[0])
    f.write(",")
    f.write(data[1])
    f.write("\n")

f.close()

# Task: If there is only one entry in the database, the program says "I've met
# 1 people".  Fix this!
