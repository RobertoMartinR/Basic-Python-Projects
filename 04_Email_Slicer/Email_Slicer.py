# I'm going to make an email slicer to obtain the username, domain and extension of a given email

def main():
    print('Hello, you are in the email slicer')
    print("")

    email_to_slice = input('Enter an email:')
    # I'm not going to control the errors to make it faster and easier
    (username, domain) = email_to_slice.split('@')
    (domain, extension) = domain.split('.')
    
    print('Username:', username)
    print('Domain:', domain)
    print('Extension:', extension)
    

while True:
    main()