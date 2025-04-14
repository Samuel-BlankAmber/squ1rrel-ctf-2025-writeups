from PIL import Image
import matplotlib.pyplot as plt

BIT_MASK_MSB = 0b10000000
BIT_MASK_LSB = 0b00000001

img = Image.open("suspicious_chicken.png").convert("RGB")
width, height = img.size

pixels = list(img.getdata())

x_coords = []
y_coords = []
for i, pixel in enumerate(pixels):
    r, g, b = pixel
    if r & BIT_MASK_LSB > 0:
        x = i % width
        y = i // width
        x_coords.append(x)
        y_coords.append(y)

plt.scatter(x_coords, y_coords, s=1)

plt.gca().invert_yaxis()
plt.axis("equal")
plt.show()
