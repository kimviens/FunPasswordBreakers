'''

Name: Kim-Frederique VIens
ID: B00793710
Date: 2 February 2020
Program description: How this program works is by using multithreading to my advantage! I use 4 for loops that goes
                     through the ascii characters determined by the built in string functions by Python. This is more
                     efficient than my bikelock program because it is doing multiple different attempts AT THE SAME TIME.
                     It goes through lowercase and uppercase letters first and then checks for cases with special
                     characters.

'''


#imports the function to use ascii lower and upper
import string

#import datetime library
from datetime import datetime

#password to attempt to find
password = input("Enter a password with length 4:")
tries = 0

#list of potential special characters in the password
specialchars = "@!#$%/_+1234567890"

#Function that is called everything my for loops generate a new attempt
def checkPassword(password, trying):

    global tries
    if trying == password:
        #prints the result to prove it
        print(trying)
        # end the timer
        later = datetime.now()

        # find the amount of time that passed
        diff = (later - now).total_seconds()

        # output the time that took to brute force
        print("Number of tries:", tries)
        print("Time taken:", diff)

        #exit the program
        exit(1)
    else:
        tries += 1
        pass

#start the timer
now = datetime.now()

#Here are all the permutations possibles using for loops that goes through for lower and upper case characters
for a in string.ascii_lowercase:
    trying = ""
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            for d in string.ascii_lowercase:
                trying1 = a + b + c + d
                trying2 = a.upper() + b + c + d
                checkPassword(password, trying1)
                checkPassword(password, trying2)
            for e in string.ascii_uppercase:
                trying3 = a + b + c + e
                trying4 = a.upper() + b + c + e
                checkPassword(password, trying3)
                checkPassword(password, trying4)

        for f in string.ascii_uppercase:
            for g in string.ascii_lowercase:
                trying5 = a + b + f + g
                trying6 = a.upper() + b + f + g
                checkPassword(password, trying5)
                checkPassword(password, trying6)

    for h in string.ascii_uppercase:
        for i in string.ascii_lowercase:
            for j in string.ascii_lowercase:
                    trying7 = a + h + i + j
                    trying8 = a.upper() + h + i + j
                    checkPassword(password, trying7)
                    checkPassword(password, trying8)
            for k in string.ascii_uppercase:
                trying9 = a + h + i + k
                trying10 = a.upper() + h + i + k
                checkPassword(password, trying9)
                checkPassword(password, trying10)

        for l in string.ascii_uppercase:
            for m in string.ascii_lowercase:
                trying11 = a + h + l + m
                trying12 = a.upper() + h + l + m
                trying13 = a.upper() + h + l + m.upper()
                checkPassword(password, trying11)
                checkPassword(password, trying12)
                checkPassword(password, trying13)

#all the permutations possible with first letter being an ascii letter and the rest is a permutation of ascii letters
#and characters from the specialchars list
for a in string.ascii_letters:
    for b in string.ascii_letters:
        for c in string.ascii_letters:
            for e in specialchars:
                trying2 = a + b + c + e
                checkPassword(password, trying2)

        for f in specialchars:
            for g in string.ascii_letters:
                trying3 = a + b + f + g
                checkPassword(password, trying3)

    for h in specialchars:
        for i in string.ascii_letters:
            for j in string.ascii_letters:
                    trying4 = a + h + i + j
                    checkPassword(password, trying4)
            for k in specialchars:
                trying5 = a + h + i + k
                checkPassword(password, trying5)

        for l in specialchars:
            for m in specialchars:
                trying6 = a + h + l + m
                checkPassword(password, trying6)
            for n in string.ascii_letters:
                trying7 = a + h + l + n
                checkPassword(password, trying7)


#all the permutations possible with first letter being a specialchar and the rest is a permutation of ascii letters
#and characters from the specialchars list
for a in specialchars:
    for b in string.ascii_letters:
        for c in string.ascii_letters:
            for e in specialchars:
                trying2 = a + b + c + e
                checkPassword(password, trying2)

        for f in specialchars:
            for g in string.ascii_letters:
                trying3 = a + b + f + g
                checkPassword(password, trying3)

    for h in specialchars:
        for i in string.ascii_letters:
            for j in string.ascii_letters:
                trying4 = a + h + i + j
                checkPassword(password, trying4)
            for k in specialchars:
                trying5 = a + h + i + k
                checkPassword(password, trying5)

        for l in specialchars:
            for m in specialchars:
                trying6 = a + h + l + m
                checkPassword(password, trying6)
            for n in string.ascii_letters:
                trying7 = a + h + l + n
                checkPassword(password, trying7)
