from PIL import Image
import pytesseract
import os

# Enter the fil name here
filename = "Screenshot 2024-07-04 132038.png"
image_path = f'C:\\Users\\ander\\Pictures\\Screenshots\\{filename}'

# Load the image from the provided path
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# output the text
output_filename = 'extracted_text.txt'
output_folder = './com_vision'
output_path = os.path.normpath(os.path.join(output_folder, output_filename))

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(f"Extracted text has been written in {output_path}")
