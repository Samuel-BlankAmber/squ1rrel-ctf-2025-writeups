from PIL import Image
import matplotlib.pyplot as plt

BIT_MASK_MSB = 0b10000000
BIT_MASK_LSB = 0b00000001

img = Image.open("suspicious_chicken.png").convert("RGB")
img_map = Image.open("treasure_map.png").convert("RGB")
width, height = img.size

pixels = list(img.getdata())
pixels_map = list(img_map.getdata())

x_coords_blue = []
y_coords_blue = []

x_coords_orange = []
y_coords_orange = []
for i, (pixel, pixel_map) in enumerate(zip(pixels, pixels_map)):
    r, g, b = pixel
    if r & BIT_MASK_LSB == 0: continue

    x = i % width
    y = i // width
    is_overlapping_with_x = pixel_map != (255, 255, 255)
    if is_overlapping_with_x:
        x_coords_orange.append(x)
        y_coords_orange.append(y)
    else:
        x_coords_blue.append(x)
        y_coords_blue.append(y)

plt.scatter(x_coords_blue, y_coords_blue, s=1, color="blue")
plt.scatter(x_coords_orange, y_coords_orange, s=1, color="blue")

plt.gca().invert_yaxis()
plt.axis("equal")
plt.show()
