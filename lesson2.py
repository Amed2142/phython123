# ask the user to enter their details
# check the datatype pf the variable
# identify what a variable is - its is a container
# phython is dynamically typed 

num1 = 5 / 6
print(num1, 'is of type:',type(num1))
num2 =2.4
print(num2, 'is of type:',type(num2))
num3 = 12j
print(num3, 'is of type:',type(num3))
message ='phython for beginers'
print(message)  
#creat alist of 4 programming language

print('Below are the top programing language in my view')
languages=["swift","java","c#","python",]

#acces element at index 0
#print(variablie name[index value])
print( languages [3])
# mutable vs immutable objects
# mutable object means they can change - lists,
# immutable means they cannot change - example strings
# modifying our list 
# apped an element to the end of our list
# syntax list_name.append(element)
languages.insert(4, "python")
languages.append("c+")
print(languages[4])
#insert an element into a list
#syntax list_name.insert(index,element)
print (languages[5])
# we can remove an element from our list 
# syntax list_name.remove(element)

#extrend the list to have go,sql
#syntax new_language.extend["element1","element2"]
#language
# create anew list of languages first to hold the two extra language  
new_languages =["go","sql"]
print(new_languages[1])
#exend the list to the original
languages.extend(new_languages)
print(len(languages))
print(languages)
