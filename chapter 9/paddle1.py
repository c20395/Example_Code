#Example 9.3 Neural-style Transfer with PaddleHub

import cv2
import paddlehub as hub

stylepro_artistic = hub.Module(name="stylepro_artistic")
result = stylepro_artistic.style_transfer(
        images=[{
            'content': cv2.imread('people1.jpeg'),
            'styles': [cv2.imread('style2.jpg')], 
            'weights':[1] 
        }],
        alpha = 1.0,
        use_gpu = False,
        visualization=True,
        output_dir='result')
import matplotlib.pyplot as plt
plt.imshow(result[0]['data'])
plt.show()
