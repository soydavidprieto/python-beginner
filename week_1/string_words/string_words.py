if __name__ == '__main__':
    print('Task 6. String words')  # TODO: [Mykyta] Why there is a blank space only here?)
# TODO: [Mykyta] We will cover that a bit later, but in Python, 
# each line should have 4 spaces inside `if block`. 
# It means, this code should be inkoke if condition is True. 
# `if __name__ == '__main__'` is True when you run it directly. 
# The problem with your code may occure when somebody will import it to their programs. 
# So for now, stick with blank spaces at each line.
    my_string = input('Enter string: ')
    my_string = my_string.split(' ')
    print('\n'.join(my_string))

 # TODO: [Mykyta] Seems you didn't split it into words yet, right?)
