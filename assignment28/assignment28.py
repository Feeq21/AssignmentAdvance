#Use labelme create a dataset from the class zoom picture for each face.
#Use as many pictures as possible.

#read image
# labelme_draw_json pic1.json

#see label in image
# labelme_draw_label_png pic1_json/label.png

import numpy as np
import PIL.Image

label_png = '../../../cv-master/advanceworkbook/assignment28/classdata/pic1_json/label.png'
lbl = np.asarray(PIL.Image.open(label_png))
print(lbl.dtype)
#print(np.unique(lbl))
print(lbl.shape)


