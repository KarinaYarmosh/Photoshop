#read image and desaturate it
#import Image lib
from PIL import Image

#open image
img = Image.open('test.txt')

#convert to grayscale
img = img.convert('L')

#save image
img.save('test2.pbm')