from PIL import Image
import pytesseract


img = Image.open('code.png')
img = img.convert('L')
result = pytesseract.image_to_string(img)
print(result)
