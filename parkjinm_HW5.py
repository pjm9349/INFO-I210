# Justin Park
# INFO - I210
# November 1st

                                            # HW 5 #


# 6.20
#Create function reverse() takes a phone book as the input. Then makes the phone number the key, instead of the value.

phonebook = {"Smith, Jane":"123-45-67",
             "Doe, John":"987-65-43",
             "Baker,David":"567-89-01"
             }

def reverse(phonebook):
    diction = {}
    for key, value in phonebook.items():
        diction[value] = key
    return diction

print(reverse(phonebook))


# 6.22
# using def function to set up a new function called mirror
def mirror(word):
    new = ""
    words = ""
# mirror string
    mirror = {'d':'b', 'b':'d', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o',
              'p':'q', 'q':'p', 'u':'u', 'w':'w', 'v':'v', 'x':'x'}
# using for loop to add from the last
    for char in range(len(word)):
        new = word[::-1]
# using for loop to check through if statements
    for char in range(len(new)):
        if new[char] not in mirror:
            return "INVALID"
            break
        if new[char] in mirror:
            words += mirror[new[char]]
    return words

print(mirror("vow"))
print(mirror("wood"))
print(mirror("bed"))



# 6.24
# using def function to call new function named names
def names():
    dic = {}
# using while True to ask input names
# and then break when nothing inputed (Just pressing enter)
    while True:
        names = input(str("Enter next name: "))
        if names == "":
            break
        elif names in dic:
            dic[names] = dic[names] + 1
        else:
            dic[names] = 1
# using for loop to know how many times of students' names are inputed.
    for key, value in dic.items():
        if value == 1:
            print("There is 1 student named", key)
        else:
            print("There are "+str(value)+" named "+key)
names()


# 6.28
# set up the dictionary
translation = {
        "hello":"Hallo",
        "apple":"pineapple",
        "coffee":"caffeine"
        }
# using def function to call new function named 'translate'
def translate(word):
# using while loop with statement to figure out words based on the dictionary    
    while True:
        translator = input("Please enter a word or STOP: ")
        if translator in translation:
            print(translator, translation[translator])
        elif translator not in translator.upper() != "STOP":
            print("____")
        elif translator.upper() == "STOP":
            break

translate(translation)


# 6.33
# import random number in a set of randrange
from random import randrange
# set a new def function to call named as diceprob
def diceprob(num):
    # set starting counting variable as "0" to count
    rolls = 0
    count = 0
# using while loop to iterate rolling dice as many as user want in the set of randrange
    while count < 100:
        dice = randrange(1,7)+randrange(1,7)
        rolls += 1
        if dice == num:
            count += 1
    print('It took {} rolls to get 100 rolls of {}'.format(rolls, num))




