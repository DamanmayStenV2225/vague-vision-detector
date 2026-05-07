from PIL import Image as img
import numpy as np
import resImg as ri
'''
path = "i1.png"
im = img.open(path)
im = im.convert('RGB')
rgbForm = np.array(im, dtype=np.int32)'''
def capture(rgbForm=0):
    print(f"{len(rgbForm[0])}x{len(rgbForm)}")
    print(rgbForm[0][0])

    minV, maxV = 0, 0
    x, y, newRGBArray = len(rgbForm[0]), len(rgbForm), []
    yal = []
    for yx in range(y):
        xvh = []
        for xx in range(x):
            xvh.append(sum(rgbForm[yx][xx]))
        yal.append(min(xvh))
        yal.append(max(xvh))
    minV, maxV = min(yal), max(yal)

    print(f"Minimum Value: {minV}, Maximum Value: {maxV}")
    cb, cw, cg = 0, 0, 0

    for ya in range(y):
        newRGBArray.append([])
        for xa in range(x):
            if sum(rgbForm[ya][xa]) >= maxV*0.66:
                newRGBArray[ya].append([255, 255, 255])
                cb+=1
            elif sum(rgbForm[ya][xa]) >= maxV*0.33 and sum(rgbForm[ya][xa]) < maxV*0.66:
                newRGBArray[ya].append([212, 212, 212])
                cg+=1
            else:
                newRGBArray[ya].append([0, 0, 0])
                cw+=1

    print(f"{len(newRGBArray[0])}x{len(newRGBArray)}")
    print(newRGBArray[0][0])
    print(f"Count black: {cb}, count white: {cw}, count green: {cg}")

    newRGBArray = np.array(newRGBArray, dtype=np.uint8)
    newIm = img.fromarray(newRGBArray, mode='RGB')
    rin = "newi1.png"
    newIm.save(rin)
    ri.downScale(rin)
    '''
    im = img.open(rin)
    ims = im.resize((im.width // 3, im.height // 3), img.BILINEAR)
    ims.save("newsi1.png")
    print("Done compressing")
    return 0'''
