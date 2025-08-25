text = input("Check if the text is palindrome")

palindrome_text = text[::-1]

if text == palindrome_text:
    print("Palindrome Text")
else:
    print("Not Palindrome")
