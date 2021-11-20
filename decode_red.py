from PIL import Image, ImageDraw, ImageFont
from numpy import asarray
import numpy as np
image = Image.open('encoded_red.png')
data = asarray(image)
img = Image.open('stegano.png')
dat = asarray(img)
ndata = []
for i in range(500):
  nrow = []
  for j in range(500):
    a,b,c = tuple(dat[i][j])
    d,e,f= tuple(data[i][j])
    if (a,b,c)==(d,e,f):
      nrow.append((255,255,255))
    else :
      nrow.append((255,0,0))
  ndata.append(nrow)
img3 = Image.fromarray(np.array(ndata).astype(np.uint8))
img3.save("decoded_red.png")
