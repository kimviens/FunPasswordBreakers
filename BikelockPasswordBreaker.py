'''

Name: Kim-Frederique VIens
ID: B00793710
Date: 2 February 2020
Program description: How this program works is a bit like a combination bike lock. But instead of the numbers 0 to 0
                     I use the ascii characters on the wheel. So I start with aaaa and then it goes baaa and then caaa
                     etc until I reach zaaa then the second wheel turns: abaa and then we continue like that until we
                     exhaust all possibilities with the lowercase letters. Then we will try with both lowercase and
                     uppercase. If we exhaust all those possibilities then we will use all the printable characters of
                     the ascii table. If it still hasn,t found the password, this program WILL EXPLODE. Just kidding it
                     prints Not Found and thats it.

                     Why is this program not the most efficient? Because it visits the set of all lowercase letters three
                     times and it visits the set of all uppercase letters two times. I am still trying to figure out a
                     better way.

                     Warning: There might be a bug for certain special characters.

                     Enjoy the brute force bike lock breaker!

'''


#import datetime library
from datetime import datetime

password = input("Enter a password with length 4:")

trying = ""
tries = 0

letter1Counter = 97
letter2Counter = 97
letter3Counter = 97
letter4Counter = 97

lowercase = True
uppercase = False

#start the timer
now = datetime.now()

while (trying != password):

    # Generate a letter using ascii
    letter1 = chr(letter1Counter)
    letter2 = chr(letter2Counter)
    letter3 = chr(letter3Counter)
    letter4 = chr(letter4Counter)
    trying = ""
    #Concatenate the 4 letters to make an attempt at guessing the password
    trying = trying+letter1+letter2+letter3+letter4
    tries += 1


    #Exhaust all lower case
    if(lowercase):

        #adds 1 to counter1 and then once counter 1 exhausted all possibilities it adds 1 to counter2 and resets counter1
        #then counter 2 does the same to counter3 and counter3 to counter4. When counter4 is exhausted we move to the
        #next step: uppercase
        letter1Counter += 1
        if (letter1Counter == 123):
            letter1Counter = 97
            letter2Counter += 1
        if (letter2Counter == 123):
            letter2Counter = 97
            letter3Counter += 1
        if (letter3Counter == 123):
            letter3Counter = 97
            letter4Counter += 1

        # Checks if we exhausted all possibilities in all lowercase
        if (letter4Counter == 123):
            lowercase = False
            uppercase = True

            #Resets the counters
            letter1Counter = 65
            letter2Counter = 65
            letter3Counter = 65
            letter4Counter = 65

    #Searching using lower AND uppercase
    if (uppercase):

        # adds 1 to counter1 and then once counter 1 exhausted all possibilities it adds 1 to counter2 and resets counter1
        # then counter 2 does the same to counter3 and counter3 to counter4. When counter4 is exhausted we move to the
        # next step: the entire ascii
        letter1Counter += 1
        if (letter1Counter == 122):
            letter1Counter = 65
            letter2Counter += 1
        if (letter2Counter == 122):
            letter2Counter = 65
            letter3Counter += 1
        if (letter3Counter == 122):
            letter3Counter = 65
            letter4Counter += 1

        # Checks if we exhausted all possibilities in uppercase+lowercase
        if (letter4Counter == 122):
            lowercase = False
            uppercase = False

            #Resets the counters for the entire ascii search
            letter1Counter = 125
            letter2Counter = 125
            letter3Counter = 125
            letter4Counter = 125

    #Entire ascii search
    if(lowercase == False and uppercase == False):

        # adds 1 to counter1 and then once counter 1 exhausted all possibilities it adds 1 to counter2 and resets counter1
        # then counter 2 does the same to counter3 and counter3 to counter4. When counter4 is exhausted we move to the
        # next step: not found
        letter1Counter -= 1
        if(letter1Counter == 32):
            letter1Counter = 125
            letter2Counter -= 1
        if (letter2Counter == 32):
            letter2Counter = 125
            letter3Counter -= 1
        if (letter3Counter == 32):
            letter3Counter = 125
            letter4Counter -= 1

        # Checks if we exhausted all possibilities in the entire ascii table
        if (letter4Counter == 32):
            print("Not found")
            break



#end the timer
later = datetime.now()

#find the amount of time that passed
diff = (later - now).total_seconds()

#output the time that took to brute force
print("Number of tries:", tries)
print("Time taken:", diff)