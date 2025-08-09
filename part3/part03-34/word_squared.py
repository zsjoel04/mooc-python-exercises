def squared(word, integer):
    index = 0
    for i in range(integer**2):
        print(f"{word[index]}",end = "")
        index += 1
        if index > len(word)-1:
            index = 0
        if (i+1) % integer == 0:
            print()






if __name__ == "__main__":
    squared("ab", 3)
















# def squared(word, integer):
#     index = 0
#     for i in range(integer):
#         if i % 2 == 0:
#             for i in range(integer):
#                 if i % 2 == 0:
#                     print(word[index], end = "")
#                     index += 1
#                     if index > len(word)-1:
#                         index = 0
#                 else:
#                     print(word[index], end = "")
#                     index += 1
#                     if index > len(word)-1:
#                         index = 0
#         else:
#             for i in range(integer):
#                 if i % 2 == 0:
#                     print(word[index], end = "")
#                     index += 1
#                     if index > len(word)-1:
#                         index = 0
#                 else:
#                     print(word[index], end = "")
#                     index += 1
#                     if index > len(word)-1:
#                         index = 0
#         print()

           

# if __name__ == "__main__":
#     squared("ab", 3)






