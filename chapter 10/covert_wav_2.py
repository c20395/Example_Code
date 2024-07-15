# Example 10.17b Convert an mp4 file to a wav file
import subprocess 

cmd1 = "E:\\ffmpeg\\bin\\ffmpeg -i Goal-GAN.mp4 Bolna.mp3"
failure = subprocess.call(cmd1, shell=True)
if failure:
    print ('Execution of "%s" failed!\n' % cmd1)

cmd2 = "E:\\ffmpeg\\bin\\ffmpeg -i Bolna.mp3 Bolna.wav"
failure = subprocess.call(cmd2, shell=True)
if failure:
    print ('Execution of "%s" failed!\n' % cmd2)
