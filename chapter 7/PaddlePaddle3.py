# Example 7.41 paddlepaddle batch background removal
import os, paddlehub as hub
module = hub.Module(name='deeplabv3p_xception65_humanseg') 
path = './imgs/' 
included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
files = [path + i for i in os.listdir(path)
         if any(i.endswith(ext) for ext in included_extensions)] 
results = module.segmentation(data={'image': files} , visualization=True, output_dir='humanseg_output/')
