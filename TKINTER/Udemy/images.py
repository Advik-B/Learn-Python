import os
from itertools import cycle
# from PIL import Image
from time import sleep
from sys import stdout


images_fol_path = r'C:\Users\advik\Pictures\Random-Pics'

images_list = []

for path2 in os.listdir(images_fol_path):
    image_path = os.path.join(images_fol_path , path2)
    images_list.append(image_path)

imgs = cycle(images_list)

for i in range(len(images_list)):
    image = next(imgs)
    # img = Image.open(image)
    # img.show()
    stdout.write(f'\rImage Path: {image}')
    sleep(.3)
