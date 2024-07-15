#Example 9.1 ISR to magnify images
#https://github.com/idealo/image-super-resolution
#pip install ISR

import numpy as np
from PIL import Image

#pip install 'h5py<3.0.0'
#pip install h5py==2.10.0
#import h5py
#h5py.run_tests()

img = Image.open('pexels-thierry-fillieul-1046492.jpg')
img.show()
lr_img = np.array(img)
from ISR.models import RDN

rdn = RDN(weights='psnr-small')
#rdn = RDN(weights='psnr-large')
#rdn = RDN(weights='noise-cancel')
sr_img = rdn.predict(lr_img)
sr_img =Image.fromarray(sr_img)
sr_img.show()
