""" Task_1."""

user_input = input("Enter a string: ")
length = len(user_input)
print("Length of the string is:", length)


# Task 2
user_input1 = str(input("Enter your repetition phrase: "))
print(user_input1 * 3)



# Task 3
namestr1 = str(input("Enter first string: "))
namestr2 = str(input("Enter second string: "))
if namestr1 == namestr2:
    print(namestr1 + " is eqaul to " + namestr2)
else:
    print(" Strings are not equal")



# Task 4

ln_string = str(input("Enter the sentence you want :"))
split_words = ln_string.split()
longest_word = max(split_words, key=len)
print( "The longest word in the string is:",longest_word, " and Its length is:", len(longest_word),)


# Task 5

my_string = "Ice bear is a bad developer. He should not code"
# Replace 'bad' with 'good'
my_string = my_string.replace("bad", "good")
# Remove 'not'
my_string = my_string.replace(" not", "")
print("Modified string:", my_string)
