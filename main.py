import cv2
from PIL import Image
from util import get_limits

red = [255, 0, 0] #Red in BGR
#Using ComputerVisual2 to utilize camera

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()

    # Code for detecting colours in camera using HSV colour space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converting RGB to HSV

    #util function called here to find the interval of colours
    lowerLimit, upperLimit = get_limits(color=red)

    # targets all the pixels from the colourspace we want to detect
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    #creating a bonding box(bbox) around the mask (a 'pillow')
    mask_box = Image.fromarray(mask)

    bbox = mask_box.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()