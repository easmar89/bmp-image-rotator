import sys

if len(sys.argv) != 2:
	print("Usage: python rotate.py <filename>")
	sys.exit(1)
else:
	filename = sys.argv[1]

with open(filename, "rb") as img:
	data = img.read()
	
WIDTH = int.from_bytes(data[18:22], "little")
HEIGHT = int.from_bytes(data[22:26], "little")
STARTING_ADDRESS = int.from_bytes(data[10:14], "little")

pixels_list = data[STARTING_ADDRESS:]
rotated_pixels= []

for row in range(HEIGHT):
	for col in range(WIDTH):
		source_row = col
		source_col = WIDTH - row - 1
		source_index = (source_row * WIDTH + source_col) * 3
		rotated_pixels.append(pixels_list[source_index:source_index + 3])

with open("output.bmp", 'wb') as output:
	output.write(data[:STARTING_ADDRESS])
	output.write(b''.join(rotated_pixels))