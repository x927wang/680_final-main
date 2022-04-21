
import os
from options.test_options import TestOptions
import cv2
import numpy as np
import util.util as ut
####This program is used to record a video using webcam

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    cap= cv2.VideoCapture(0)
    width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer= cv2.VideoWriter(opt.video_save, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
    while True:
        ret,frame= cap.read()
        writer.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    writer.release()
    cv2.destroyAllWindows()