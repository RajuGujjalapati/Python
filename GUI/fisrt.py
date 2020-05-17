from PIL import Image
img=Image.open('moun.jpg')
print(img.size)
width, height=img.size
print(width)
print(height)
print(img.format_description)#format
img.save('imga.png')
"""
im=Image.new('RGBA',(100,200),'purple')#creates purple box with width=100 and height=200
im.save('purpleimage.png')

im2=Image.new('RGBA',(200,200))#no color
im2.save('transparent.png')
"""
#Last two values of the below represents the horizontal and vertical.
#If we increases the value then it increases the hori and verti size.
croppedIm=img.crop((100,100,500,1000))#give clear values
croppedIm.save('cropped.png')
img=Image.open('moun.jpg')
imgCopyIm=img.copy()
imgCopyIm.paste(croppedIm,(0,0))#pasting image on image
print(imgCopyIm.size)
imgCopyIm.paste(croppedIm,(950,500))
#we can give multiple images on a single image in difeerent places.
imgCopyIm.save('pasted.png')
imgwidth, imgheight=img.size
crowidth, croheight=croppedIm.size
copytwo=img.copy()
for left in range(0, imgwidth, crowidth):
    for top in range(0, imgheight, croheight):
        print(left, top)
        copytwo.paste(img,(left, top))
copytwo.save('last.png')
