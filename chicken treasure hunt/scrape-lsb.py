from PIL import Image

BIT_MASK_LSB = 0b00000001

img = Image.open("suspicious_chicken.png").convert("RGB")
img_map = Image.open("treasure_map.png").convert("RGB")
width, height = img.size

pixels = list(img.getdata())
pixels_map = list(img_map.getdata())

bits = ""
for i, (pixel, pixel_map) in enumerate(zip(pixels, pixels_map)):
    if pixel_map == (255, 255, 255): continue

    r, g, b = pixel
    bits += str(r & BIT_MASK_LSB)

blocks = [bits[i:i + 8] for i in range(0, len(bits), 8)]
byte_data = bytearray([int(block, 2) for block in blocks])

with open("byte_data.bin", "wb") as f:
    f.write(byte_data)
