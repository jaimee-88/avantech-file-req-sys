from PIL import Image
import numpy as np

# Load the image
img = Image.open('static/images/avantech-logo.png')

# Convert to RGBA if not already
img = img.convert("RGBA")

# Get image data
data = np.array(img)

# Define white color threshold (adjust if needed)
# This will make white and near-white pixels transparent
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Create mask for white pixels (where R, G, B are all high)
white_threshold = 240
white_mask = (r > white_threshold) & (g > white_threshold) & (b > white_threshold)

# Set alpha channel to 0 (transparent) for white pixels
data[:,:,3] = np.where(white_mask, 0, 255)

# Create new image with transparent background
img_transparent = Image.fromarray(data)

# Save the result
img_transparent.save('static/images/avantech-logo.png', 'PNG')

print("✓ White background removed successfully!")
print("Logo saved as: static/images/avantech-logo.png")
