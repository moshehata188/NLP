"""
Mohamed Mohamed Shehata Shehata Badawy
FCAI|DU Level 4 - CS department  
Task 1  ( Natural Language Processing )
"""
from nltk.tokenize import sent_tokenize, word_tokenize

# Text
# NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all,NLTK is a free, open source, community-driven project.


def output_using_split(text):
    return text.split('\n')


def main():
    text = input("Enter the text: ")
    while True:
        choice = input(
            "Choose one of the following options:\n1. Tokenized words\n2. Tokenized sentences\n3. Output using split function\n4. Quit\n")

        if choice == '1':
            print("Output:", word_tokenize(text))
        elif choice == '2':
            print("Output:", sent_tokenize(text))
        elif choice == '3':
            print("Output:", output_using_split(text))
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
