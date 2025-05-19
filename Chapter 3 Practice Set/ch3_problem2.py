#Write a python program to fill in a letter template given below with name and date
letter = '''
Dear <|Name|>
You are selected
<|Date|>
'''

print(letter.replace("Name","Tony").replace("Date","06-03-2025"))