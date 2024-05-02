# I'm going to create a very basic calculator using functions for every of the common operations: add, substract, multiply and divide

def add(a: int, b: int): 
    sum = a + b
    print(f'{a} + {b} = {sum}')
    
def sub(a: int, b: int): 
    sum = a - b
    print(f'{a} - {b} = {sum}')
    
def mul(a: int, b: int): 
    sum = a * b
    print(f'{a} * {b} = {sum}')
    
def div(a: int, b: int): 
    sum = a / b
    print(f'{a} / {b} = {sum}')
    

while True: 
    print("""
             1. Addition
             2. Substraction
             3. Multiplication
             4. Division
             5. Exit
        """)
    choice = int(input("Make your choice from the options given above: ")) # We need to make an int input, otherwise the program is not gonna work

    if choice == 1:
        print("Your choice is Addition")
        a = int(input('Choose the first number:'))
        b = int(input('Choose the second number: '))
        add(a, b)
    elif choice == 2:
        print("Your choice is Substraction")
        a = int(input('Choose the first number:'))
        b = int(input('Choose the second number: '))
        sub(a, b)
    elif choice == 3:
        print("Your choice is Multiplication")
        a = int(input('Choose the first number:'))
        b = int(input('Choose the second number: '))
        mul(a, b)
    elif choice == 4:
        print("Your choice is Division")
        a = int(input('Choose the first number:'))
        b = int(input('Choose the second number: '))
        div(a, b)
    elif choice == 5:
        print('Quitting')
        quit()
