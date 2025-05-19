'''
Walrus operator (:=), allows you to assign various to variables as part of an expression.

'''

if (n := len(my_list)) > 5:
    print(f"List is too long ({n} elements, expected <= 5)")