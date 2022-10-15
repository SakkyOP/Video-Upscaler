import os
import shutil
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
        shutil.rmtree(os.path.join(inPath,file))

def save_video(inPath, outPath, originalVideoPath, fps):
    temp_vid_dir = ".\\data\\temp_vids"
    os.makedirs(temp_vid_dir, exist_ok= True)
    
    collections = [ os.path.join(inPath, collection) for collection in os.listdir(inPath) ]
    
    for collection in collections:
        images = [ os.path.join(collection, image) for image in os.listdir(collection) ]
        images_to_video(images, fps, temp_vid_dir+"\\temp_vid_"+str(collections.index(collection))+".avi")

    clips = [ VideoFileClip(os.path.join(temp_vid_dir, clip)) for clip in os.listdir(temp_vid_dir) ]

    out_video = concatenate_videoclips([*clips])
    out_video.write_videofile(outPath, fps=fps, codec= 'rawvideo')
    
    VideoFileClip(outPath).set_audio(VideoFileClip(originalVideoPath).audio)

def images_to_video(frames, fps, outPath):
    
    vid_frames = []
    
    for frame in frames:
        vid_frames.append(ImageClip(frame).set_duration(1/fps))
        
    out_video = concatenate_videoclips(vid_frames, method = "compose")
    out_video.write_videofile(outPath, fps= fps, codec = "rawvideo")
    