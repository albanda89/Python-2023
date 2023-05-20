phrase = "ReDI school is awesome! Yes ReDI is really cool"


# Split the phrase into words
words = phrase.split()

# Count the occurrences of 'ReDI'
count = 0
for word in words:
    if word == 'ReDI':
        count += 1

print("The word 'ReDI' occurs", count, "time(s) in the phrase.")