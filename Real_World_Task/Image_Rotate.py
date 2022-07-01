import PIL
from PIL import Image
with Image.open("C:/Users/sarav/Downloads/Elephant.jpeg") as im:
    im.rotate(45).show()