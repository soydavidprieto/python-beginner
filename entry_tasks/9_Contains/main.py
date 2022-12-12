        #9
if __name__ == '__main__':
    message = input('Enter your favorite quotation: ')
    find_letter = input('Enter the letter you want to check: ')
    if find_letter in message:
        print('true. this letter present in the string')
    else:
        print('false. there is no such a letter')