from PIL import Image
with Image.open("C:/Users/sarav/Downloads/Elephant.jpeg") as im:
    new_im = im.resize((640,480))
    new_im.save("C:/Users/sarav/Downloads/example_resized.jpg")
