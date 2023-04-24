'''为了获得正常样本，从splitimage.py生成的结果中删除有红色的数据，算是一个数据粗筛'''
import os
import cv2
from PIL import Image
src_dir = "G:\\splited\\EappDataDataFactoryDataWorkshopxieimagestrain - 副本"
#src_dir = "G:\\splited\\ceshi"
def deleteRedImg(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            src = os.path.join(root, file)
            if not isNormal(src):
                os.remove(src)
def isNormal(file):
    im = Image.open(file)
    width = im.size[0]
    height = im.size[1]
    for h in range(0, height):
      for w in range(0, width):
        r,g,b = im.getpixel((w, h))
        if(r> 15+max(g,b)):
            return False
    return True

if __name__ == '__main__':
    deleteRedImg(src_dir)
