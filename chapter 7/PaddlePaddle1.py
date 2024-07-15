# Example 7.39 paddlepaddle background removal
import os, paddlehub as hub
huseg = hub.Module(name='deeplabv3p_xception65_humanseg')
files = ['./imgs/01.jpg']
results = huseg.segmentation(data={'image': files} , visualization=True, output_dir='humanseg_output/')
