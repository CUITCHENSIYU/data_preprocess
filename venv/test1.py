import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os.path
import glob
import scipy.misc
from PIL import Image
from tensorflow.python.platform import gfile

img=tf.gfile.FastGFile('test.jpg','rb').read()

with tf.Session() as sess:
    img = tf.image.decode_png(img)
    img = tf.image.adjust_brightness(img, -0.001)
    img=img.eval()
    # img = tf.image.convert_image_dtype(img, dtype=tf.float32)
    img=img/255

    print(img)
    plt.figure(1)

    plt.imshow(img)
    plt.show()

# INPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\test1\\3\\"
# OUTPUT_DATA="E:/DeepLearn/SingleCellImage/venv\\test2\\3/"
# ###########格式转换############################
# def convert(file):
#     img=tf.gfile.FastGFile(file,'rb').read()
#
#     with tf.Session() as sess:
#         img_data=tf.image.decode_bmp(img)
#         img_data=tf.image.convert_image_dtype(img_data,dtype=tf.uint8)
#         encoded_img=tf.image.encode_png(img_data)
#         name = os.path.basename(file)[0:23]
#         with tf.gfile.GFile(OUTPUT_DATA+name+'.png','wb') as f:
#             f.write(encoded_img.eval())
# for file in glob.glob(INPUT_DATA+"*.BMP"):
#      print(file)
#      convert(file)




###########图片剪切##################
# INPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\pap_smear_image\\test.jpg"
# OUTPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\pap_smear_image\\test2.jpg"
#
# image_raw_data_jpg=tf.gfile.FastGFile(INPUT_DATA,'rb').read()
# with tf.Session() as sess:
#     img_data_jpg = tf.image.decode_jpeg(image_raw_data_jpg)
#     img_data = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.uint8)
#     img_data = tf.image.resize_image_with_crop_or_pad(img_data, 56, 56)
#
#     img_data = tf.image.convert_image_dtype(img_data, dtype=tf.uint8)
#     encoded_img=tf.image.encode_jpeg(img_data)
#     with tf.gfile.GFile(OUTPUT_DATA,'wb')as f:
#         f.write(encoded_img.eval())