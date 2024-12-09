import interface
import superSonicSnailMail
import ayoThatsCap

'''
ALGORITHM // OVERVIEW
1. ask for email
2. let user take their photo
3. send the photo to user's email address
'''

# variable with user's email address
receiver = interface.requestEmail() # creates window with entry widget


# variable with file name ("path") as a string, represents photograph
frame = ayoThatsCap.cvShowCap() # starts running the webcam display, gains value only after user presses SPACE

# sends photo to specified email address
superSonicSnailMail.sendEmail(frame, receiver)