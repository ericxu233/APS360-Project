import os
from PIL import Image 
import PIL 


dir = "bigdata/portraits"
counter = 1

for filename in os.listdir(dir):
    if filename.endswith(".jpg"):
        pic = os.path.join(dir, filename)
        im1 = Image.open(pic)
        im1 = im1.resize((64, 64))
        kk = "newbig/kk" + str(counter) + ".jpg"
        im1.save(kk)
        print("printing kk" + str(counter))
        counter += 1

        
