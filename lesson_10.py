# Task 1
# Write s a Python program that reads the "input.txt" file, counts the occurrences of each word, and prints the word along with its count, while ignoring case sensitivity:

## Since there  is no contet in the file we need to write a content first and then do the following
## Write a sentence to the file
sentence = "Aruni is ReDI student"

with open('input.txt', 'w') as file:
    file.write(sentence)

# Read the contents from the file
with open('input.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

    # Convert the content to lowercase to ignore case sensitivity
    # content = content.lower()

    # Split the content into words
    words = content.split()

    # Count the occurrences of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the word and its count
    for word, count in word_counts.items():
        print(f'{word}: {count}')


