import cv2, urllib, time, os
import numpy as np

print "Connecting..."

ip = "Put IP of that computer Here"

try:
    req = urllib.urlopen('http://' + ip + '/1.png')
    print "Connected"

    while True:
	    req = urllib.urlopen('http://' + ip + '/1.png')
	    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	    img = cv2.imdecode(arr,-1)
	    cv2.imshow('Desktop-2',img)
	    k = cv2.waitKey(10)
	    if  k  == 27:
		    break
	    time.sleep(2)

except:
    print "Can't Connect NOW"
