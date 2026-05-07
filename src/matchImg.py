from PIL import Image as img
import numpy as np

def matching(ari):
    ai = np.array(ari, dtype=np.uint8)
    ig = img.fromarray(ai, mode="RGB")
    svi = "si.png"
    ig.save(svi)
    im0 = img.open(svi)
    im0 = im0.resize((im0.width//3, im0.height//3), img.BILINEAR)
    rgbForm0 = np.array(im0, dtype=np.int32)
    im1 = img.open("newsi1.png")
    rgbForm1 = np.array(im1, dtype=np.int32)


    minV, maxV = 0, 0
    x, y, cc = len(rgbForm0[0]), len(rgbForm0), 0
    wv = x*y
    yal = []
    for yx in range(y):
        xvh = []
        for xx in range(x):
            xvh.append(sum(rgbForm0[yx][xx]))
        yal.append(min(xvh))
        yal.append(max(xvh))
    minV, maxV = min(yal), max(yal)

    for ya in range(y):
        for xa in range(x):
            val = rgbForm1[ya][xa]
            if val[0] == 255:
                if sum(rgbForm0[ya][xa]) >= maxV*0.66:
                    cc+=1
            elif val[0] == 212:
                if sum(rgbForm0[ya][xa]) >= maxV*0.33 and sum(rgbForm0[ya][xa]) < maxV*0.66:
                    cc+=1
            else:
                cc+=1

    if cc/wv >= 0.9:
        print("Match")
    else:
        print("No match")
