import string

def my_layers(layers):
    alphabet = string.ascii_uppercase
    my_str = list(reversed(alphabet[:layers]))
    length = len(my_str) * 2 - 1
    disposable_list = []
    saved_list = [my_str[0]]
    num = 0
    for x in range(length):
        if x == 0 or x == length -1:
            for i in range(length):
                disposable_list.append(my_str[0])    
            for letter in disposable_list:
                print(letter, end = "")
            print()
            disposable_list = []            
        else:
            if x + 1 < layers:
                saved_list.append(my_str[x]) # Ez ele kell egy if hogy csak akkor menjen bele ha x + 1 < layers
                for z in saved_list:
                    disposable_list.append(z)
                while not len(saved_list) * 2 + num == length:
                    disposable_list.append(saved_list[-1])
                    num += 1
                num = 0
                for z in list(reversed(saved_list)):
                    disposable_list.append(z)
                for letter in disposable_list:
                    print(letter, end = "")
                print()
                disposable_list = []
            elif x + 1 == layers:
                for z in saved_list:
                    disposable_list.append(z)
                disposable_list.append(my_str[x])   
                for z in list(reversed(saved_list)):
                    disposable_list.append(z)
                for letter in disposable_list:
                    print(letter, end = "")
                print()
                disposable_list = []
            else:
                if x > layers:
                    saved_list.pop(-1)
                for z in saved_list:
                    disposable_list.append(z)
                while not len(saved_list) * 2 + num == length:
                    disposable_list.append(saved_list[-1])
                    num += 1
                num = 0
                for z in list(reversed(saved_list)):
                    disposable_list.append(z)
                for letter in disposable_list:
                    print(letter, end = "")
                print()
                disposable_list = []



a = int(input())
my_layers(a)




