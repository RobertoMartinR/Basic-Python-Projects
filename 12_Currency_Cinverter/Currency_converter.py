# I'm going to create an € to $ coverter

def main():
    
    euro = eval(input('Introduce the quntity of euro to convert: '))
    
    dolars = convert_to_dolars(euro)
    
    print(f'{euro} euros are {dolars} dolars')
    
convert_to_dolars = lambda euro: euro * 1.08

main()
