import cv2

url = 'rtsp://admin:Tony0000@192.168.1.108/cam/realmonitor?channel=1&subtype=00&authbasic=YWRtaW46YWRtaW4='
cap = cv2.VideoCapture(url)

num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/img' + str(num) + '.png', img)
        print("image saved!")
        num += 1

    cv2.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()