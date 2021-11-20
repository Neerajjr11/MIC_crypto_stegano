from PIL import Image, ImageDraw, ImageFont
from numpy import asarray
import numpy as np
image = Image.open('image_text_red.png')
data = asarray(image)
img = Image.open('stegano.png')
dat = asarray(img)
#print(data)
ndata = []
for i in range(500):
  nrow = []
  for j in range(500):
    a,b,c = tuple(dat[i][j])
    if tuple(data[i][j])==(255,0,0):
      nrow.append((a+1,b,c))
    else :
      nrow.append((a,b,c))
  ndata.append(nrow)
img2 = Image.fromarray(np.array(ndata).astype(np.uint8))
img2.save("encoded_red.png")

