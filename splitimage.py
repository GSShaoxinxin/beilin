'''功能：将某一目录srcdir下所有图片切成n*m块。并将切后图片按照文件件目录结构拷贝到指定文件夹dstdir
参考了https://blog.csdn.net/zaibeijixing/article/details/129895422 和 https://www.cnblogs.com/jyxbk/p/7805042.html
'''
"""
srcdir_list = {
"I:\\4.松材线虫\\2019.10.27-广西桂林灵川县\\4.地点四-县城-116县道右边\\正射\\1.可拼接",
"I:\\4.松材线虫\\2019.10.29-广西贺州\\1.地点一-平桂区老寨山右边\\正射\\2.200m航线-1200x700",
"I:\\4.松材线虫\\2019-12-7-福建福州市青口镇\\1.地点一-大义头-玄天上帝庙附近\\正射-病树特写",
"I:\\4.松材线虫\\20210515-0516-广东韶关始兴县\\20210515-0516-广东韶关-车八岭自然保护区\\地点2\\航线扫描",
"I:\\4.松材线虫\\20210515-0516-广东韶关始兴县\\20210516-广东韶关-始兴县城附近\\地点一",
"I:\\4.松材线虫\\20210515-0516-广东韶关始兴县\\20210515-0516-广东韶关-车八岭自然保护区\\地点8",
"I:\\4.松材线虫\\20210515-0516-广东韶关始兴县\\20210516-广东韶关-始兴县城附近\\地点二"
}
"""
import os
import cv2
from PIL import Image
import imghdr



#srcdir_pre = "I:\4.松材线虫"
src_list = {"E:\\appData\\DataFactory\\DataWorkshop\\xie\\images\\train"}
#src_list = {"I:\\4.松材线虫\\测试裁剪图片"}


dst_root = "G:\\splited"


def split_files(src_list, dst_root,height_n,width_m):

    for src_root in src_list:
        i=src_root.replace("\\", "").replace(":","")
        for root, dirs, files in os.walk(src_root):
            for file in files:
            #print(root)
                src = os.path.join(root, file)
                destination_path = os.path.join(dst_root, i)
                splitimage(src,height_n,width_m,destination_path)

def splitimage(src, rownum, colnum, dstpath):
    if not os.path.isdir(dstpath):#如果路径不存在就新建
        os.makedirs(dstpath)
    if not imghdr.what(src): #如果不是图片就不要切割了
        return
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext))
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')




if __name__ == '__main__':
    split_files(src_list,dst_root,5)


