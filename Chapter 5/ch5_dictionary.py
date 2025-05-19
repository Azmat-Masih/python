#Dictionary in python are muteable
#Stores value in form of key.value pair

# It is unorder
# It is indexed
# Cannot contain duplicate key

my_dictionary = {
    "name":"Azmat",
    "age": 25,
    "BloodGroup" : "A+",
    "DateOfBirth" : 12/8/1999
}

numbers_dictionary = {
    "Azmat" : 100,
    "Tony" : 56,
    "Bill" : 12,
    "Elon" : 67
}

print(type(my_dictionary))

# Methods of Dictionary
print(numbers_dictionary.keys()) #Gives us keys of dic
print(numbers_dictionary.values()) #Gives us values of dic

numbers_dictionary.update({"Bill":54}) #updates the value of given key
print(numbers_dictionary)

print(my_dictionary.items()) #gives the dic in tuple form

print(numbers_dictionary.get("Elon")) #Gives the value of of given key # if value dosen't exits, gives us none
print(numbers_dictionary.get("Jake")) # if value dosen't exits, gives us none

print(numbers_dictionary["Bill"]) # Gives the value of the given key 
print(numbers_dictionary["jake"]) # If value dosen't exits, gives us error