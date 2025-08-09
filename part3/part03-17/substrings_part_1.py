word =input("") # abc
lenght = len(word) # 3
index = 1
for i in range(lenght-1): # 1, 2, 3
    if index == 1:
        print(word[0])
    index += 1
    print(word[0:index])
    
