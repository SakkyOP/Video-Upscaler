import cv2
from cv2 import dnn_superres

def upscale_image(frame, modelPath, model_name, scale):
    sr = dnn_superres.DnnSuperResImpl_create()
    
    sr.readModel(modelPath)
    
    # Build OpenCV with CUDA support (using CMake)
    # sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    
    sr.setModel(model_name, scale)
    
    out_frame = sr.upsample(frame)
    
    return out_frame