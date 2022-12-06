if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input('''
    Select operation:
    + Addition
    - Distraction
    * Multiplication
    / Division
    == Equals
    != Not Equals
    > Greater than
    < Less than
    >= Greater than or equals to
    <= Less than or equals to
    ** Exponentiation
    // Floor division
    % Modulo
    or enter another operation
    ''')
    if op == '+':
        print(f'{a} {op} {b} is {a + b}')
    elif op == '-':
        print(f'{a} {op} {b} is {a - b}')
    elif op == '*':
        print(f'{a} {op} {b} is {a * b}')
    elif op == '/':
        print(f'{a} {op} {b} is {a / b}')
    elif op == '==':
        print(f'{a} {op} {b} is {a == b}')
    elif op == '!=':
        print(f'{a} {op} {b} is {a != b}')
    elif op == '>':
        print(f'{a} {op} {b} is {a > b}')
    elif op == '<':
        print(f'{a} {op} {b} is {a < b}')
    elif op == '>=':
        print(f'{a} {op} {b} is {a >= b}')
    elif op == '<=':
        print(f'{a} {op} {b} is {a <= b}')
    elif op == '**':
        print(f'{a} {op} {b} is {a ** b}')
    elif op == '//':
        print(f'{a} {op} {b} is {a // b}')
    elif op == '%':
        print(f'{a} {op} {b} is {a % b}')
    else:
        print(f"'{op}' is invalid operation")
