# ----------| Rotation |----------


from PIL import Image, ImageDraw
import math
from math import sin, cos

input_img = Image.open('messi5.jpg')
input_pixels = input_img.load()

ouput_img = Image.new("RGB",  input_img.size)
draw = ImageDraw.Draw(ouput_img)

angle = math.radians(50)
center_x = input_img.width/2
center_y = input_img.height/2


for x in range(input_img.width):
    for y in range(input_img.height):
        xp = int((x - center_x) * cos(angle) - (y - center_y)*sin(angle) + center_x)
        yp = int((x - center_x) * sin(angle) + (y - center_y)*cos(angle) + center_y)
        
        if 0 <= xp < input_img.width and 0 <= yp < input_img.height:
            print("xp, yp :", str(xp) + ", " + str(yp))
            draw.point((x, y), input_pixels[xp, yp])


ouput_img.show()
