import random
import os

capital = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 's', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

def randomletter(text):
        y = random.choice(text)
        return y

length = input("How long should the password be?")
if type(length) == "<class 'int'>" and length > 0 and length % 2 == 0:

    pwd = ""

    for l in range(int(length)):
        x = random.randint(1,6)
        if x == 1 or x == 5:
            first = randomletter(capital)
        elif x == 2 or x == 6:
            first = randomletter(small)
        else:
            first = randomletter(numbers)
        pwd = pwd+first

    print("Your", length, "digit password is:")
    print(pwd)
else:
    print("Enter a Valid Positive integer")