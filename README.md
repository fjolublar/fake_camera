Code Example:

``` python
import cv2 as cv
from fake_camera import FakeCamera  # import the class

fake_cam_object = FakeCamera()      # create an instance of the class

while True:
       canvas_view = fake_cam_object.read_fake_image()   #call the new image from the fake camera
       cv.imshow("Moving Image", canvas_view)  
       time.sleep(1/10)
       if cv.waitKey(1) & 0xFF == ord('q'):                                    
           break
```
