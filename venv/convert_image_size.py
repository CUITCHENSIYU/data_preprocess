import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os.path
import glob
import scipy.misc
from PIL import Image
from tensorflow.python.platform import gfile

# INPUT_DATA='pap_smear_image/carcinoma_in_situ'
# OUTPUT_DATA='processed_pap_smear_image/carcinoma_in_situ'
INPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\smear_convert_format\\正常-柱状细胞\\"
OUTPUT_DATA="E:\\DeepLearn\\SingleCellImage\\venv\\smear_convert_size\\正常-柱状细胞"
# # 获取一个子目录中的所有图片数据
# extensions = ['jpg', 'jpeg', 'JPG', 'JPEG','BMP','bmp']  # 列出所有扩展名
# file_list = []
# for extension in extensions:
#     # INPUT_DATA是数据集的根文件夹，其下有五个子文件夹，每个文件夹下是一种花的照片；
#     # dir_name是这次循环中存放所要处理的某种花的图片的文件夹的名称
#     # file_glob形如"INPUT_DATA/dir_name/*.extension"
#     file_glob = os.path.join(INPUT_DATA, 'carcinoma_in_situ', '*.' + extension)
#     # extend()的作用是将glob.glob(file_glob)加入file_list
#     # glob.glob()返回所有匹配的文件路径列表,此处返回的是所有在INPUT_DATA/dir_name文件夹中，且扩展名是extension的文件
#     file_list.extend(glob.glob(file_glob))
def convert(file,outdir,width=72,height=72):
    img=Image.open(file)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(file)))
    except Exception as e:
        print(e)
for file in glob.glob(INPUT_DATA+"*.jpg"):
    print(file)
    convert(file,OUTPUT_DATA)






