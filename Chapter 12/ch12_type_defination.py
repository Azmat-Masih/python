'''
Type Defination:

'''

n : int = 4 #Defining that n is a integor

name : str = "Tony" #Defining that name is string

#now the program will tell us that we defines n as a intergar and we have to use intergor operations on it.
# n.

#Now the program will tell us that we defines name as a str and we have to use string operations on it.
# name.


'''
Types in functions.
'''

def sum(a: int, b: int) -> int:
    return a + b


sum(3,5)


'''
Importing advance typing
'''
from typing import List, Union, Tuple, Dict

# List of intergers
numbers: List[int] = [1,3,4,5,6]

# Tuples of a string and an integers
person: Tuple[str, int] = ("Alice", 34)

# Dictionary with string keys and intergers values
scores: Dict[str, int] = {"Alice": 30, "Bob" : 67}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 #Also valid


# These annotations help in making the 
# code self documenting and allow developers 
# to understand the data structure used at a glance.