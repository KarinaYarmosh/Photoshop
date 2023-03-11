from photoshop.pnm.pbm import PBMImage

#open pbm
img = PBMImage('test_raw.pbm')
for i in range(img.height):
    for j in range(img.width):
        print(img.get_pixel(j, i), end=' ')
    print()
