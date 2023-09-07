import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    #Images ,Videos, Live Videos
     # Calculate the new width and height based on the scale factor
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    #Finally, the code resizes the input frame using the OpenCV function cv.resize. 
    # It takes three arguments: the original frame, the desired dimensions (specified by the dimension tuple), 
    # and the interpolation method (cv.INTER_AREA in this case, which is suitable for downscaling).
    #  The function then returns the resized frame.


def Changref(width,height):
    #Live Videos
    captureVideo.set(3,width)
    captureVideo.set(4,height)

#Reading Image

img = cv.imread('Opencv/Photos/cat_large.jpg')  # Read and Show
reframed_img=rescaleFrame(img)
cv.imshow('Cat',img)  #(name , Pixel) to show
cv.imshow("Cat_img",reframed_img)

#opencv doesnot have image editor.If you have Larger images it possible go off the screen. so  rescale and resize is tho fix the issue. 
cv.waitKey(0)  #delay  for show by enter key

#   ===================
#Reading Video

# Create a VideoCapture object and open the video file
captureVideo= cv.VideoCapture('Opencv/Videos/dog.mp4')
#captureVideo= cv.VideoCapture(0)   : int value 0 means first prefered camera in your system,1 ,2.. etc means all camera add to your system with preference.
# Start an infinite loop to continuously read and display video frames
while True:
    # Read a frame from the video capture
    isTrue, frame = captureVideo.read() #This line reads a frame from the video capture object 
    # 'captureVideo and stores it in the variables isTrue and frame. isTrue is a boolean variable that indicates whether the frame was successfully read, and frame contains the actual video frame.
    frame_resize=rescaleFrame(frame)

    #Show
    cv.imshow("Dog",frame)
    cv.imshow("Dog",frame_resize)
      # Check if the 'd' key is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        #This part of the code checks for user input. It uses cv.waitKey(20) to wait for 20 milliseconds for a key press.
        #  If the 'd' key is pressed (ASCII value of 'd' is 100), ord('d') will be equal to 100,
        #  and cv.waitKey(20) & 0xFF will evaluate to 100 as well. In that case, the break statement is executed, and the loop exits,
        # effectively stopping the video playback.
    
# Release the video capture object
captureVideo.release()

# Close all OpenCV windows
cv.destroyAllWindows()
