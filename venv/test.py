import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os.path
import glob
import scipy.misc
from PIL import Image
from tensorflow.python.platform import gfile

INPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\test1\\"
OUTPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\test2\\"

######调整对比度和亮度##########################

def convert(file):
    image_raw_data_jpg = tf.gfile.FastGFile(file, 'rb').read()

    with tf.Session() as sess:
        img_data_jpg = tf.image.decode_jpeg(image_raw_data_jpg)
        img_data_jpg = tf.image.random_contrast(img_data_jpg,0.6,1.4)
        crop = tf.image.resize_image_with_crop_or_pad(img_data_jpg, 72, 72)

        plt.imsave(os.path.join(OUTPUT_DATA,os.path.basename(file)),crop)

for file in glob.glob(INPUT_DATA+"*.jpg"):
    print(file)
    convert(file)


############剪切###################
# def convert(file,outdir,width=56,height=56):
#     image_raw_data_jpg = tf.gfile.FastGFile(file, 'rb').read()
#
#     with tf.Session() as sess:
#         img_data_jpg = tf.image.decode_bmp(image_raw_data_jpg)
#         img_data_jpg = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.float32)
#         crop = tf.image.resize_image_with_crop_or_pad(img_data_jpg, 72, 72)
#
#         plt.imsave(os.path.join(OUTPUT_DATA,os.path.basename(file)),crop)
#
# for file in glob.glob(INPUT_DATA+"*.bmp"):
#     print(file)
#     convert(file,OUTPUT_DATA)



# img=cv2.resize(img,(72,72),interpolation=cv2.INTER_CUBIC)

# # 垂直翻转
# flipped=cv2.flip(img,0)
# cv2.imshow("abc",flipped)
# cv2.imwrite("E:\\DeepLearn\\SingleCellImage\\venv\\processed_pap_smear_image\\test"+"1.bmp",flipped)
# cv2.waitKey(0)

# #旋转###################
# (h,w)=img.shape[:2]
# center=(w/2,h/2)
# M=cv2.getRotationMatrix2D(center=center,angle=90,scale=1)
# newimg=cv2.warpAffine(img,M,(w,h))
# cv2.imshow("change",newimg)
# cv2.waitKey(0)

# #镜像变换########################
# img_info=img.shape
# img_weight=img_info[1]
# img_height=img_info[0]
# dst=np.zeros(img.shape,np.uint8)
# for i in range(img_height):
#     for j in range(img_weight):
#         dst[i,j]=img[img_height-i-1,j]
# cv2.imshow('lod',dst)
# cv2.waitKey(0)
