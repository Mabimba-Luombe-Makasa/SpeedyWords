
# Title and sub heading
print("WELCOME TO SPEEDY WORDS")
print("Helping you count your text...\n")

# This function counts the words in the document
def word_count(content):
    total_words = content.split()
    return len(total_words)

# The while loop rens until user enters correct file name.
while True:
    try:
        # Prompts user to enter file name
        file_name = input("Please enter the FILE NAME of the document you want to count words for (Including file name extension): \n")

        # Checks if user wants to exit application
        if file_name.lower() == 'exit':
            print("Thank you for using the program. \nExiting....")
            break

        # Reads the file data
        with open(file_name, "r") as file:
            content = file.read()

        # After reading and counting the words  it prints the total number
        print("The total number of words in the document is ", word_count(content), "words.\n")

    # Error Handling if file not found
    except FileNotFoundError:
        print("File not found. Please enter the correct FILE NAME or 'exit' to quit.\n")

    # Error Handling for permission issues
    except PermissionError:
        print("Permission denied. Please make sure you have the necessary permissions to access the file.\n")

    # Error Handling for encoding issues
    except UnicodeDecodeError:
        print("Error decoding the file. Please make sure the file is in a readable format.\n")
