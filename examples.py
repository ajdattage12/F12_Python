#BASIC CALCULATOR 
num1 = input("Enter a number: ")
num2 = input('Enter another number: ')
result = float(num1) + float(num2) 
#python auto converts input to a string. Must convert to a number. 
#int() only works with whole numbers. float() accepts decimals. 

print(result)


#MAD LIBS GAME
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
adjective = input("Enter a adjective: ")
feeling = input("Enter a feeling: ")

print("roses are " + color)
print(plural_noun + " are blue")
print("You make be " + adjective + " but ")
print("I still " + feeling + " you")



