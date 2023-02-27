#!python3

'''
##### Task 8
Read through the file **example2.py** for information on using the math module.
Calculate the length of a hypotenuse given 2 variables
Set the value of a to 5
Set the value of b to 8

Determine the length of the hypotenuse and store it into a variable called c
print the value of c

You may use either the ** operator or math.pow(x,y) for your exponents
You may use either math.sqrt(x) or the exponent to the power of 0.5 for your square root

 '''

import math
print("This calculator is used to find a missing side length in a right triangle")
a = 0.0
b = 0.0
c = 0.0

def ina():
    a = float(input("Enter length of the first side, if unknown, type \"0\""))
    if a < 0:
        print("Side lengths can\'t be negative ya clown, try again:")
        ina()
    else:
        inb()

def inb():
    b = float(input("Enter length of the second side, if unknown\, type \"0\""))
    if b < 0:
        print("This calculator will allow negative sides just as soon as you figure out how to measure a negative length, try again stupid:")
        inb()
    else:
        inc()

def inc():
    c = float(input("Enter length of the hypoteneuse, if unknown, type \"0\""))
    if c < 0:
        print("Now just how the hell is a negative length supposed to be the longest side of a triangle? let's try that one again:")
        inc()
    if a >= c or b >= c:
        print("Hypoteneuse has to be the longest side, this isn't a multi-dimensional shape")
        inc()
    else:
        check()

def check():
        unknown = 0

        if a==0:
            unknown = unknown + 1

        if b==0:
            unknown = unknown + 1

        if c==0:
            unknown = unknown + 1   

        if unknown >= 2:
            print("not enough sides are known, triangle cannot be solved")

def Pythagoras():
    ina()
    
Pythagoras()
