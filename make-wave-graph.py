import sys
import os
import cv2
import numpy as np

_str_list = []
with os.scandir('dpx') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            _str_list.append(entry.name)
imgs = []

for _i in _str_list:
    fileName = "dpx/" + _i
    imgs.append(cv2.resize(cv2.imread(fileName), (1, 1080)))
    if len(imgs) is 2:
        hmerge = np.hstack((imgs))
        imgs = []
        imgs = [hmerge]
    else:
        continue

cv2.imwrite("out.jpg", imgs[0])
sys.exit()
