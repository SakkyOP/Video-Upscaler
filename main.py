import os
import cv2
import traceback # for error handling
from moviepy.editor import VideoFileClip
from upscaler import upscale_image
from combine_vid import save_video, clear_dir

CURRENT_DIRECTORY = os.getcwd()

IN_VIDEO = ".\\data\\in_video"
OUT_VIDEO = ".\\data\\out_video"
OUT_FRAMES = ".\\data\\out_frames"
[os.makedirs(dir, exist_ok=True) for dir in [IN_VIDEO, OUT_VIDEO, OUT_FRAMES]]

IN_VIDEO = IN_VIDEO + "\\video_3.mp4"
OUT_VIDEO = OUT_VIDEO + "\\upscale_video_1.avi"

MODEL_PATH = os.path.join(CURRENT_DIRECTORY,"models","FSRCNN-small_x4.pb")
MODEL_NAME = "fsrcnn"
SCALE = 4
FPS = 30

video = cv2.VideoCapture(IN_VIDEO)

frame_count = 0

frames = []

try:
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame_count += 1
        
        up_frame = upscale_image(frame, MODEL_PATH, MODEL_NAME, SCALE)

        collectiondir = OUT_FRAMES+ f"\\collection{frame_count // 100}"
        os.makedirs(collectiondir, exist_ok= True)
        
        cv2.imwrite(collectiondir+"\\frame_no_{0}.jpg".format(frame_count, frame_count % 100), up_frame)
        
        print(f"No. of Frames processed {frame_count}")

except KeyboardInterrupt:
    print("Keboard Interrupt!")
    
except Exception as e:
    print("An error occurred: {0}".format(e))
    print(traceback.format_exc())

try:
    save_video(OUT_FRAMES, OUT_VIDEO, IN_VIDEO, FPS)
except Exception as e:
    print("An error occurred: {0}".format(e))
    print(traceback.format_exc())

video.release()

clear_dir(OUT_FRAMES)
# VideoFileClip(OUT_VIDEO).set_audio(VideoFileClip(IN_VIDEO).audio)
    