# Prompt the user to choose whether to count with spaces or without spaces
while True:
    count_with_spaces = input("Count with spaces? (yes/no): ").lower()
    if count_with_spaces in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no' only.")

# Prompt the user to input a word
word = input("Enter a word: ")

# Count the word with or without spaces
if count_with_spaces != "yes":
    # Remove spaces and tabs
    word = word.replace(" ", "").replace("\t", "")
total_alphabets = len(word)
# Print the output
print("Total Alphabets:", total_alphabets)
