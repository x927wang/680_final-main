Title: CS680 Final Project

Name:   Guanting Pan AND
        Xuetong Wang

Note:   - This is the repo for the cycleGAN and video transfer program
        - To reproduce the result, we strongly recommand to use a GPU  to run the experiment
        - The input.mp4 in the root is the input video we used to run the experiment
        - The output.mp4 in the root is the result of the experiment
        - the neural_style_transfer.ipynb is not included in this project, it is just a document we used to play around with neural style transfer (i.e., another image style transfer algorithm)
        - This project is an implementation of CycleGAN, for more information on cycleGAN, please refer to the original CycleGAN github repo: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix

Here is the command line to run the video transfer program

1. Please install all the necessary packages, such as "cv2".

2. Run "cd pytorch-CycleGAN-and-pix2pix"

2. (OPTIONAL) you can record you own video by using the webcam by running:
    "python3 record_video.py --video_save \<direction for saving the recored video\>"
    Note: Please hit Esc on the keyboard if you want to stop the recording

3. start the transformation by running:
    "python3 video_transfer.py --name vango_light_3 --model test --no_dropout --video_input \<direction for the input video\> --video_output \<direction for saving the output video\>"
