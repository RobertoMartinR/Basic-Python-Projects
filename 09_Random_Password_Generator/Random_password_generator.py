# Let's create a random password generator

# Import of the modules needed
import string
import random

# Define the available characters to choose from to make the password
characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

# Function definition
def random_password_generator(): 
    password_length = int(input('How loung would you like your password to be? : '))
    
    random.shuffle(characters) # Shuffle to make it as random as possible
    
    password = [] # Empty variable to store de password
    
    # Selection of the characters
    for x in range (password_length): 
        password.append(random.choice(characters))
        
    random.shuffle(password) # Again we shuffle to put the characters chosen in a random position 
    password = "".join(password) # Join the characters to make them appear together and not separated by a comma
    print(password) # Finally print it
    
option = input('Do you want to generate a password ? (Yes/No):') # Ask if the user wants to generate a password and take a decision based on his answer
    
if option == 'Yes':
        random_password_generator()

elif option == 'No':
        print('Program ended')
        quit()
else:
        print('Type a valid answer (Yes/No)')
        quit()

