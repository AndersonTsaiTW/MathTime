from PIL import Image
import pytesseract
import os

# Enter the fil name here
filename = input("請輸入檔案名稱（包含副檔名）: ")
image_path = os.path.join(r'C:\Users\ander\OneDrive\Pictures\螢幕擷取畫面', filename)

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
