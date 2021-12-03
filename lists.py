#WORKING WITH LISTS aka arrays
#lists have starting index of 0. 
my_siblings = ["Barrett", "Trent", "Lani", "Karissa", "Trever", "Vince"]
print(my_siblings[2])

#prints the last item of the list
print(my_siblings[-1])

#grabbing elements from a list first number is index position, 
#second number is the range but won't be included. *Up to but not inlcuding specificed index*
print(my_siblings[2: 6])


#Using extend allows you to add one array on to a second array. 
sister_in_laws = ["Jen", "Julie", "Madison"]
my_siblings.extend(sister_in_laws)
print(my_siblings)

#Using append allows you to add single items on to the list
my_siblings.append("Jared")
print(my_siblings)

#Using insert allows you to add items to a specific part of a list
#the first paramater is the index location
#The second paramater is what you want to insert. 
my_siblings.insert(0, "Ben")
print(my_siblings)

#to remove an element from a list remove get rid of a single element
my_siblings.remove("Ben")
print(my_siblings)

#MORE LIST MODIFICATIONS
#clear removes EVERY element from the list
#pop removes only the LAST element from the list

#to find a specific value use index. It will return the index location of that value.
print(my_siblings.index("Trent"))

#


