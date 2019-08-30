import numpy as np
from PIL import Image
import scipy.misc
import tensorflow as tf

data=np.load('processed_smear_data/smear_dataset.npy',allow_pickle=True)
x1,x2,x3,x4=data

x1=np.array(x3[0])
print(x1[0])

# a=np.array(x1[2])
# print(a)
# a=a*72
# img=Image.fromarray(a.astype(np.uint8))
# img.show()
# img.save('test.png')


