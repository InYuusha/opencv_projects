import cv2

videocapture=cv2.VideoCapture("C:\\New folder\\cute.mp4")

fps=videocapture.get(cv2.CAP_PROP_FPS)
size=(int(videocapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
      
          int(videocapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videowriter=(cv2.VideoWriter("C:\\Users\\op\\Desktop\\this.avi",cv2.VideoWriter.fourcc('I','4','2','0'),fps,size))

success,frame=videocapture.read()
while success:
    
    videowriter.write(frame)
    
    success,frame=videocapture.read()
