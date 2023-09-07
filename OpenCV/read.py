import cv2 as cv

#Reading Images - Section 1
'''
img = cv.imread('Opencv/Photos/cat_large.jpg')  # Read and Show
cv.imshow('Cat',img)  #(name , Pixel) to show

#opencv doesnot have image editor.If you have Larger images it possible go off the screen. so  rescale and resize is tho fix the issue. 
cv.waitKey(0)  #delay  for show by enter key

'''
#Reading Video - Section 1
# Create a VideoCapture object and open the video file
captureVideo= cv.VideoCapture('Opencv/Videos/dog.mp4')
#captureVideo= cv.VideoCapture(0)   : int value 0 means first prefered camera in your system,1 ,2.. etc means all camera add to your system with preference.
# Start an infinite loop to continuously read and display video frames
while True:
    # Read a frame from the video capture
    isTrue, frame = captureVideo.read() #This line reads a frame from the video capture object 
    # 'captureVideo and stores it in the variables isTrue and frame. isTrue is a boolean variable that indicates whether the frame was successfully read, and frame contains the actual video frame.
    cv.imshow("Dog",frame)
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

#error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow' - open cv ran out of frames
