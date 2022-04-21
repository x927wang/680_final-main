
import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
import cv2
import torch
import numpy as np
import util.util as ut

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    if opt.eval:
        model.eval()
    
    the_video = cv2.VideoCapture(opt.video_input)
    out_video = cv2.VideoWriter(opt.video_output,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (512,512))
    data = {"A": None, "A_paths": None}

    while True:
        ret, frame = the_video.read()
        if frame is None:
            break
        #Crop the frame in the video
        frame = cv2.resize(frame, (256,256), interpolation=cv2.INTER_AREA)
        ##
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.array([frame])
        frame = frame.transpose([0,3,1,2])
        data['A'] = torch.FloatTensor(frame)
        model.set_input(data)  # unpack data from data loader
        model.test()
        result_image = model.get_current_visuals()['fake']
        result_image = ut.tensor2im(result_image)
        result_image = cv2.cvtColor(np.array(result_image), cv2.COLOR_BGR2RGB) 
        result_image = cv2.resize(result_image, (512, 512)) 
        out_video.write(result_image)
        cv2.imshow('frame', result_image)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cv2.destroyAllWindows()