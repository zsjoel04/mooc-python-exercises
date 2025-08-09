words = ""
last_word = ""
while True:
    word = input("Please type in a word:")
    if last_word == word:
        print(words)
        break
    last_word = word
    if word == "end":
        print(words)
        break
    words += word + " "
    
    
    
   
