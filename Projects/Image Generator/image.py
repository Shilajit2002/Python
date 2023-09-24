from PIL import Image, ImageFilter
import os

# Open the original image
original_image = Image.open('E:\\Python\\Code\\Projects\\Image Generator\\Capture.jpg')

# Create a directory to save the generated images
if not os.path.exists('E:\\Python\\Code\\Projects\\Image Generator\\soupImages'):
    os.makedirs('E:\\Python\\Code\\Projects\\Image Generator\\soupImages')

# Apply various filters and save the generated images
filter_names = ['BLUR', 'CONTOUR', 'EDGE_ENHANCE', 'EMBOSS', 'SHARPEN']
for filter_name in filter_names:
    filtered_image = original_image.filter(getattr(ImageFilter, filter_name))
    output_path = os.path.join('E:\\Python\\Code\\Projects\\Image Generator\\soupImages', f'{filter_name.lower()}_image.jpg')
    filtered_image.save(output_path)

print("Generated images saved in the 'generated_images' folder.")
