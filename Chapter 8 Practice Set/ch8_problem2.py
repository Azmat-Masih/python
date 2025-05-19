# Write a program using function to convert celsius to fornhigh

# (celsius * 9/5) + 32

# def convert_celsius_to_fornhigh(celsius):
#     celsius_ = (celsius * 9/5) + 32 #formula for converting celsius to fahrenheit
#     return celsius_

# celcius_input = float(input("write the celcius number here: "))

# fahrenheit_to_celsius = convert_celsius_to_fornhigh(celcius_input)
# print(f"the celsius {celcius_input} °C  converted to fornhigh is, ", fahrenheit_to_celsius + "°F")


# Fahrenheit to celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = 5*(fahrenheit - 32)/9 #formula for converting fahrenheit to celsius
    return celsius


user_input = int(input("write fahrenheit here: "))
result_ = fahrenheit_to_celsius(user_input)
print(f"This is the celsius {round(result_,2)}°C of fahrenheit of {user_input}°F .")