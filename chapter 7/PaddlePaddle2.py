# Example 7.40 paddlepaddle batch background removal
import os, paddlehub as hub
huseg = hub.Module(name='deeplabv3p_xception65_humanseg')
path = './imgs/' 
files = [path + i for i in os.listdir(path)]
results = huseg.segmentation(data={'image': files} , visualization=True, output_dir='humanseg_output/') 
