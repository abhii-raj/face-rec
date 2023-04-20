import cv2 as cv

img = cv.imread('images\cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame , scale = 0.75 ):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos\dog.mp4')
while True:
    isTrue , frame = capture.read() # basically reads the video frame by frame
    
    frame_resized = rescaleFrame(frame, scale=.2)


    cv.imshow('Video', frame) # displaying video
    cv.imshow('videoresized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): # to break out ( basically means press d to break out of window )
        break
capture.release()
cv.destroyAllWindows()
