def word_dictionary():
    new_word_dictionary = {
        "hi" : "a greeting",
        "hello" : "a greeting",
        "bye" : "a farewell",
        "goodbye" : "a farewell",
        "thank you" : "an expression of gratitude",
        "you're welcome" : "an expression of gratitude",
        "sorry" : "an expression of regret",
        "excuse me" : "an expression of regret",
    }
    while True:
        word = input("Enter a Word : ")
        if word == "":
            break
        if word in new_word_dictionary:
            print(word, ":", new_word_dictionary[word])

word_dictionary()