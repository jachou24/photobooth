import cv2 as cv

# basically webcam as a variable
cap = cv.VideoCapture(0) # 0 = whatever computer's default camera is set to

'''
function that shows the webcam display until photo is taken
UI: user can press SPACE to 'take the photo'
returns the frame (image) at that moment the window closes
'''
def cvShowCap():
    while True: # run forever until...
        r, frame = cap.read() # unpacking capture, r is irrelevant here, frame=the image you see on the webcam at any given moment
        cv.imshow('Use SPACE to take photo!', frame) # displays webcam on screen for every time capture is read (updated)

        if cv.waitKey(1) == ord(' '): # ...until user presses SPACE to take photo
            imgPath = "temp_image.jpg"
            cv.imwrite(imgPath, frame) # solution for variable type error: creates a jpg of frame
            break
    
    # shut off the camera and close the webcam display
    cap.release()
    cv.destroyAllWindows()

    '''
    returning image file name ("path") as a usable string
    --> main.py --> = frame
    '''
    return imgPath