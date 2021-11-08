# ----------| Resize |----------

from PIL import Image

img = Image.open("messi5.jpg")
print("Old dimens :", img.size)

factor = 2

W = img.width
H = img.height

newW = int(W*factor)  # width
newH = int(H*factor)  # height

newImage = Image.new("RGB", (newW, newH))
for col in range(newW):
    for row in range(newH):
        p = img.getpixel((col/factor, row/factor))
        newImage.putpixel((col, row), p)

newImage.show()
print("New dimens :", newImage.size)
