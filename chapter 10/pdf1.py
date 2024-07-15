# Example 10.25 Image to PDF
# --- Save one image to pdf --------------------------------------------------
#https://datatofish.com/images-to-pdf-python/
from PIL import Image

image1 = Image.open(r'images\000_000.jpg')
im1 = image1.convert('RGB')
im1.save(r'myFirstImage1.pdf')

# --- Save several images to pdf --------------------------------------------------
image1 = Image.open(r'images\000_000.jpg')
image2 = Image.open(r'images\000_010.jpg')
image3 = Image.open(r'images\000_020.jpg')
im1 = image1.convert('RGB')
im2 = image2.convert('RGB')
im3 = image3.convert('RGB')
imagelist = [im2,im3]
im1.save(r'mySecondImage1.pdf',save_all=True, append_images=imagelist)
