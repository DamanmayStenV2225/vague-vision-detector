from PIL import Image as img

def downScale(i):
    im = img.open(i)
    ims = im.resize((im.width//3, im.height//3), img.BILINEAR)
    ims.save("newsi1.png")
    print("Done compressing")