# fake_camera
A python library to simulate a Camera. A moving Image in the screen.

# Usage

``` python
import cv2 as cv
from fake_camera import Fake_Camera  # import the class

fake_cam_object = Fake_Camera()      # create an instance of the class

while True:
    canvas_view = fake_cam_object.read_fake_image()   #call the new image from the fake camera
    cv.imshow("Moving Image", canvas_view)  
                                   
    time.sleep(1/10)
   
    if cv.waitKey(1) & 0xFF == ord('q'):                                    
        break
        ```
