from PIL import Image
from pytesseract import pytesseract

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"D:\tesseract\tesseract.exe"
image_path = r"./static/images/FULL-09166401824.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the tesseract
# executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to
# image_to_string() function
# This function will
# extract the text from the image
text = pytesseract.image_to_string(img)
text_size= len(text)

# Displaying the extracted text
print(text[:-1])

