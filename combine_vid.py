
import os
from moviepy.editor import *

"""
images = []

data_dir = ".\\data\\out_frames"
filenames = os.listdir(data_dir)

for i in range(len(filenames)):
    images.append(ImageClip(os.path.join(data_dir, filenames[i])).set_duration(1/23.5))
    
out_video = concatenate_videoclips(images, method= 'compose')
out_video.write_videofile("video.avi", fps=23.5, codec= 'rawvideo')
"""
def clear_dir(inPath):
    for file in os.listdir(inPath):
        os.unlink(os.path.join(inPath, file))

def save_video(inPath, outPath, originalVideoPath, fps):
    images = []
    
    for i in range(len(os.listdir(inPath))):
        images.append(ImageClip(os.path.join(inPath, os.listdir(inPath)[i])).set_duration(1/fps))

    out_video = concatenate_videoclips(images, method= 'compose')
    out_video.write_videofile(outPath, fps=fps, codec= 'rawvideo')
    
    VideoFileClip(outPath).set_audio(VideoFileClip(originalVideoPath).audio)