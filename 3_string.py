# @Sen ----------Exercise 3 ---------

# Expeted to Print only Even  characters from the string users input.


string=input('Enter your string here: ')


print(f'Original string: {string} ')

print('Printing Even characters .....\n')
# using for loop through string and print only even characters.
for i in range(0, len(string), 2):
    # printing the characters
    print(string[i])