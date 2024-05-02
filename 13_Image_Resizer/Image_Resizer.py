from PIL import Image

def image_resizer(size1, size2):
    image=Image.open('') # We specify inside the brackets the path to the image we want to resize
    
    print(f'Current size: {image.size}')
    
    resized_image = image.resize((size1, size2))
    
    resized_image.save('13_Image_Resizer/mifoto' + str(size1) + '.JPG')
    
size1 = int(input('Enter Width:'))
size2 = int(input('Enter Lenght:'))
image_resizer(size1, size2)