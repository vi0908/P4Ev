import re
x= input('My favorite two numbers are: ')
y=re.findall('[0-9]+',x)
print('So, your favorite numbers are: ')
for number in y:
    print(number)