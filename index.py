# print("Hello World")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

character_name = "Tom"
character_age = "50"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")

character_name = "Mike" #can change the varibale value halfway through. Code reads top to bottom. 
character_age = "40"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# TYPES OF VALUES 
# strings = "Anything written in quotes"
# numbers = any integer or decimal number 5 or 5.99
# boolean = true or false value 

print("ARIELL\nJEAN\nDATTAGE") #adds line breaks 
print("SPENCER\"DATTAGE") #prints actual quotation mark
print("HAILEY\DATTAGE") #prints blackslash

phrase = "Kaden tore his ACL while mountain biking"
print(phrase)

#METHODS AND FUNCTIONS
print(phrase + " with Spencer.") #concation
print(phrase.lower()) #makes entire string lowercase
print(phrase.isupper()) #returns boolean value. This particular method is cheking for uppercase

phrase_two = "Hannah is taking a ceramics class"
print(phrase_two.upper())
print(phrase_two.upper().isupper()) #allows you to chain methods together. All methods must be invoked with (). 

phrase_three = "Addyson wants to go to college in Italy"
print(len(phrase_three)) #this function checks the length of the phrase. 
#python starts at a 0 index.
print(phrase_three[0]) #allows you to get specific characters

phrase_four = "The twins are named, Liam and Emmett"
print(phrase_four.index("twins")) #returns the index of that values

phrase_five = "Ariell is taking a Javascript class"
print(phrase_five.replace("Javascript", "Python")) #allows you to replace values in a string. 

#WORKING WITH NUMBERS
print(-120.872) #print the whole or negitave number or decimal directly
print(6 + 2.87) #does basic mathematical equations
print(4 * 5 + 2) #follows order of opertaions
print(4 *(5 + 2)) #takes in parenthesis for consideration. allows you to change order. 
print(10 % 3) #gives us the remainder. % = mod. 10 / 3 = 3 remainder of 1. so 10%3 = 1 

#store numbers in variable
my_number = 21
print(my_number)

print(str(my_number) + " is my favorite number")#converts number to string

#FUNCTIONS
my_num = -5
print(abs(my_num)) #returns the absolute value of the number

print(pow(3, 2)) #returns the first numbers to the value of the second number. example= 3 ^ 2
print(max(4,6)) #returns the largest or max number
print(min(104, 31)) #returns the smallest or min number
print(round(3.7)) #returns the number rounded to the nearest whole number

from math import *

print(floor(3.7)) #returns the whole number and drops the decimal
print(ceil(5.1)) #return the next whole number regardless of decimal value
print(sqrt(81)) #returns the square root

#GETTING INPUT FROM USERS
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + ".")
