from PIL import Image, ImageDraw, ImageFont
from numpy import asarray
import numpy as np
#print(data)
a = []
for i in range(500):
  b = []
  for j in range(500):
    b.append((255,255,255))
  a.append(b)
img = Image.fromarray(np.array(a).astype(np.uint8))
myFont = ImageFont.truetype('FreeMono.ttf', 80)
d1 = ImageDraw.Draw(img)
d1.text((125, 230), "PLANE", font=myFont, fill =(0, 0, 255))
img.save("image_text_blue.png")