def func(s, subs):
    verify = subs in s
    if verify == False:
        print("The substring does not occur twice in the string.")
        return
    lenght = len(subs)
    #elsot megkeressuk
    find1 = s.find(subs) 
    #levagas
    cutchars = find1 + lenght
    levagott = s[cutchars:]
    # kereses a levagottban
    verify = subs in levagott
    if verify == False:
        print("The substring does not occur twice in the string.")
        return
    find2 = levagott.find(subs) 
    print(f"The second occurrence of the substring is at index {cutchars + find2}.")
string = input("")
substring = input("")
func(string, substring)

## ererdeti: 
# ABCghjABC
# 012345678

# ABCghjABC
# 012345678
#find az 0
#levagunk elejebol find 0 plusz substring hosszat




# verify = substring in string
# find = string.find(substring) 
# print(f"find is {find}")
# verify = substring in string
# string = string[find + lenght:]
# print(f"string is {string}")
# if verify == True:
#     print(find + lenght)
# else:
#     print("The substring does not occur twice in the string.")

















# string = input("Please type in a string: ") 
# substring = input("Please type in a substring: ") 
# # find = string.find(substring)
# lenght = len(string)
# sub_len = len(substring)
# index = 0
# second_occurance = 0
# for i in range(lenght):
#     if string[index] == substring[0]:
#         second_occurance += 1
#         if second_occurance == 1:
#             index += sub_len
#         elif second_occurance == 2:
#             print(f"The second occurrence of the substring is at index {index}.")
#             break





















