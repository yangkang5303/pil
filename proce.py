from PIL import Image
import pytesseract
im = Image.open('yanzheng.png')
aa = pytesseract.image_to_string(im,lang='eng')
print(aa)