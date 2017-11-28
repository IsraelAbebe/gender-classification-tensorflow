# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import cv2
import subprocess

TRAINSET = "haarcascade_frontalface_alt.xml"
DOWNSCALE = 4
age = ""
web_cam = cv2.VideoCapture(-1)
classifier = cv2.CascadeClassifier(TRAINSET)

if web_cam.isOpened():
    rval, frame = web_cam.read()

else:
    rval = False
    print "here"


while rval:
    # detect faces and draw bounding boxes
    minisize = (frame.shape[1] / DOWNSCALE, frame.shape[0] / DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier.detectMultiScale(miniframe)
    if len(faces) == 0:
        cv2.putText(frame, "face not detected.", (250, 250),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255))
        age = " "

    for f in faces:
        x, y, w, h = [v * DOWNSCALE for v in f]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))
        cv2.putText(frame, age, (x, y),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255))
    cv2.putText(frame, "Press C to see how old you look after your face is detected.", (5, 25),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255))


    cv2.imshow("preview", frame)

    # get next frame
    rval, frame = web_cam.read()
    if cv2.waitKey(1) & 0xFF == ord('c') and len(faces) != 0:
        cv2.imwrite("cache/1.jpg", frame)
        subprocess.check_output(['python', 'facecrop.py',"cache/1.jpg"])
        result = subprocess.check_output(
            ['python', 'predict.py', '--model', 'model/1vggface-ft_gender.h5', '--image', 'cache/1_cropped_.jpg'])



        if result[:-1] == '0':
            text = "Female"
        elif result[:-1] == '1':
            text = "male"
        print "capture " + text

        age = text

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
