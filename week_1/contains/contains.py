word = input ('insert a word: ')
letter = input('Insert the letter that you would like to find: ')
 
# returns first occurrence of Substring
result = word.find(letter)
print('Substring ', letter, ' found at index: ', result)
 
