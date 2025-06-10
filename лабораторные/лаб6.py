
from PIL import Image, ImageOps

image = Image.open('example.jpg')
inverted_image = ImageOps.invert(image)
inverted_image.save('inverted_example.jpg')