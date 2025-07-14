name = "yash kanzariya"

print(len(name)) # length of string

print(name.endswith("h")) # starts and end give boolean values true or false
print(name.startswith("h"))
print(name.capitalize()) #captilize starting charcter only
print(name.upper()) #all upper case
print(name.lower()) #all lower case
print(name.title())#cap first char of each word
print(name.count("y"))#count the no. of given charcter
print(name.find(" "))#give the index of first occurrence of that word
print(name.replace("y","x")) #replace al given char.

#for bold
print("\033[1mThis is bold text\033[0m")
