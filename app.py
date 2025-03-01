import sys
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python bw_convert.py <image_file_name>")
    sys.exit(1)

image_file = sys.argv[1]
image_name = image_file.split(".")[0]

try:
    image = Image.open(image_file)
except IOError:
    print("Error in loading image!!")
    sys.exit(1)

bw_image = image.convert('L')
bw_image.save("bw_" + image_name + ".png")
