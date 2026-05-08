letter = 'Partik'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))   

# Multiline String
multiline_string = '''I am a Partik and enjoy programming.
Mi chiamo partik e mi piache il programmazione.
Vengo da padova'''

print(multiline_string)

first= 'Piazzola'
last = 'sul brenta'
space = ' '
full = first + space + last
print(full) 

# Accessing characters in strings by index
language = 'Partik'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n