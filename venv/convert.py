import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os.path
import glob
import scipy.misc
from PIL import Image
from tensorflow.python.platform import gfile

INPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\test1\\1\\"
OUTPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\test2\\1\\"
def convert(file):
    img = tf.gfile.FastGFile(file, 'rb').read()

    with tf.Session() as sess:
        img_data=tf.image.decode_jpeg(img)
        name=os.path.basename(file)[0:23]
        img_data=tf.image.convert_image_dtype(img_data,dtype=tf.uint8)
        img_data = tf.image.random_contrast(img_data,2.0,2.5)
        img_data=tf.image.adjust_brightness(img_data,0.1)
        print(img_data)
        img_data=tf.image.rgb_to_grayscale(img_data)
        img_data = tf.image.convert_image_dtype(img_data, dtype=tf.uint8)
        encoded_img=tf.image.encode_jpeg(img_data)
        with tf.gfile.GFile(OUTPUT_DATA+name+'.png','wb')as f:
            f.write(encoded_img.eval())

for file in glob.glob(INPUT_DATA+"*.png"):
    print(file)
    convert(file)