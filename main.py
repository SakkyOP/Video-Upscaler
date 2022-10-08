import os
from turtle import width
import cv2
from moviepy.editor import VideoFileClip
from upscaler import upscale_image

CURRENT_DIRECTORY = os.getcwd()

IN_VIDEO = ".\\data\\in_video\\video_1.mp4"
OUT_VIDEO = ".\\data\\out_video\\upscale_video.avi"
MODEL_PATH = os.path.join(CURRENT_DIRECTORY,"models","FSRCNN_x4.pb")
MODEL_NAME = "fsrcnn"
SCALE = 4
FPS = 24

video = cv2.VideoCapture(IN_VIDEO)

frame_count = 0

while True:
    ret, frame = video.read()
    if ret:
        break
    
    frame_count += 1
    up_frame = upscale_image(frame, MODEL_PATH, MODEL_NAME, SCALE)
    
    width, height, channels = up_frame.shape
    
    if frame_count == 1:
        out_video = cv2.VideoWriter(OUT_VIDEO, cv2.VideoWriter_fourcc(*'DIVX'), FPS, (width, height))
    
    out_video.write(up_frame)
    
    print(f"No. of Frames processed {frame_count}")
    
out_video.release()
video.release()

VideoFileClip(OUT_VIDEO).set_audio(VideoFileClip(IN_VIDEO).audio)
    