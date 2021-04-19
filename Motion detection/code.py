import cv2

# start camera

cap = cv2.VideoCapture(0)

tap1 = cap.read()[1]
tap2 = cap.read()[1]
tap3 = cap.read()[1]

gray1 = cv2.cvtColor(tap1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(tap2,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(tap3,cv2.COLOR_BGR2GRAY)

# now creating imge diff
def img_diff(x,y,z):
    d1 = cv2.absdiff(x,y)
    d2 = cv2.absdiff(y,z)
    # absilute diff d1-d2
    finalimg = cv2.bitwise_and(d1,d2)
    return finalimg


while cap.isOpened():
    status, frame = cap.read()
    # cv2.imshow('live',frame)
    motionimg = img_diff(gray1,gray2,gray3)

    # replacing image frame
    gray1 = gray2
    gray2 = gray3
    gray3 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # passing live image to gray

    cv2.imshow('live',frame)
    cv2.imshow('motion', motionimg)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

# distroy
cv2.destroyWindow()
cap.release()