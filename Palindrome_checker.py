def is_palindrome(word):
    # Remove spaces and convert to lowercase for a better check
    word = word.replace(" ", "").lower()
    
    # Compare the word to its reverse
    if word == word[::-1]:
        print(True)
    else:
        print(False)

# Example usage:
user_input = input("Please enter a word: ")
is_palindrome(user_input)
