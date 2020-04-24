# This python script helps to access the camera,record and export a video output file.
# By Malay @ 2020

#           ! - Warning - ! 
# Must have opencv installed -->> pip install opencv-contrib-python
# Must understand the scripts written and then consider modifing it to meet requirement.
# Must have latest python installed on your system.


# Importing the modules.
import cv2

is_recording = False
# Enter the camer id.
print("Enter 0 for system camera\nEnter 1 for external camera")
cam_num = int(input("Enter the camera Num: "))

print("\n q:quit \t r:record \t s:screenshot")
print("[Warning]: Press the button in the new window. Not here. Entering name for screenshot will be here.")
# Read video from camera.
cp = cv2.VideoCapture(cam_num)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))

while(True):
    ret,frame = cp.read()
    cv2.imshow('live cam', frame)

    if is_recording == True:
        out.write(frame)
    if cv2.waitKey(10) & 0xFF == ord('r'):
        if is_recording == True:
            is_recording = False
            print("Recording stopped")
        elif is_recording == False:
            is_recording = True
            print("Recording started")
        else:
            pass
    elif cv2.waitKey(10) & 0xFF == ord('s'):
        name = str(input("Enter name of screen shot: "))
        cv2.imwrite(f'./{name}.jpg',frame)
    elif cv2.waitKey(10) & 0xFF == ord('q'):
        break

out.release()
cp.release()
cv2.destroyAllWindows()