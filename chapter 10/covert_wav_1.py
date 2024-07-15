# Example 10.17a Convert an mp4 file to a wav file

import os 

cmd1 = "E:\\ffmpeg\\bin\\ffmpeg -i Goal-GAN.mp4 Bolna.mp3"
failure = os.system(cmd1)
if failure:
    print ('Execution of "%s" failed!\n' % cmd1)

cmd2 = "E:\\ffmpeg\\bin\\ffmpeg -i Bolna.mp3 Bolna.wav"
failure = os.system(cmd2)
if failure:
    print ('Execution of "%s" failed!\n' % cmd2)
