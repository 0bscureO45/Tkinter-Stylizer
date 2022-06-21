from PIL import Image, ImageDraw
from requisites import *
from prerequisites import *

images = []

for i in range(0, 50, 1):
    image = rounded_rectangle(width=400, height=100, radius=i)
    images.append(image)
    
for i in range(50, 0, -1):
    image = rounded_rectangle(width=400, height=100, radius=i)
    images.append(image)

images[0].save('pillow.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=20, loop=0)