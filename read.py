import cv2 as cv 
# takes an image and returns it as a matrix of pixels 

 # img = cv.imread('images\cat_large.jpg')
# displays the eimage as a new window  , name of window is cat and img czo whose pixel to display 

 # cv.imshow('Cat', img )
# it waits for a  certain interval  of time to load the image if pressed 0 it waits for infinite interval of time

 # cv.waitKey(0)
# if u have large images its probably going of screen 

# for playong videos  
#  we will integer  in video capture if camera is connected to ur computer for inbuilt we use 0 and for further cams we keep going on like 1 2 3..
#  we can do it other wawy by adding path 
capture = cv.VideoCapture('videos\dog.mp4')
while True:
    isTrue , frame = capture.read() # basically reads the video frame by frame
    cv.imshow('Video', frame) # displaying video

    if cv.waitKey(20) & 0xFF==ord('d'): # to break out ( basically means press d to break out of window )
        break
capture.release()
cv.destroyAllWindows()

