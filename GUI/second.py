from PIL import Image
"""lion=Image.open('lion.jpg')
width, height=lion.size
quar=lion.resize((int(width/2), int(height/2)))
quar.save('cutted.jpg')
#it gives the resized half image, no details will be eliminated during re-sizing.
sve=lion.resize((width+500, height+300))
sve.save('saved.png')
lion.rotate(6).save('lionrotate.png')
lion.rotate(45).save('lionrotate180.png')
lion.rotate(55,expand=True).save('lionrotate270.png')
#using expand may print the clean result
lion.transpose(Image.FLIP_TOP_BOTTOM).save('flip.png')
nimg=Image.new('RGBA',(1900,990))
nimg.getpixel((0,0))
for x in range(1900):
    for y in range(400):
        nimg.putpixel((x,y),(128,128,128,255))
from PIL import ImageColor
for x in range(1900):
    for y in range(400,800):
        nimg.putpixel((x, y),ImageColor.getcolor('aliceblue','RGBA'))
nimg.save('try.png')
"""


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
import os
os.makedirs('withLogo', exist_ok=True)
   # Loop over all files in the working directory.
for filename in os.listdir('.'):
    
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
          or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
          # Calculate the new width and height to resize to
    if width > height:
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE
print('Resizing %s...' % (filename))
im =im.resize((width, height))
print('Adding logo to %s...' % (filename))
im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
im.save('see.png')































    
