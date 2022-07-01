from flask import Flask, render_template, Response
import cv2
app=Flask(__name__)
camera = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def find_and_blur(bw, color): 
    # detect al faces
    faces = cascade.detectMultiScale(bw, 1.04, 4)
    # get the locations of the faces
    for (x, y, w, h) in faces:
        # select the areas where the face was founds
        roi_color = color[y:y+h, x:x+w]
        # blur the colored image
        blur = cv2.GaussianBlur(roi_color, (101,101), 0)
        # Insert ROI back into image
        color[y:y+h, x:x+w] = blur            
    
    # return the blurred image
    return color



def gen_frames():  
    while True:
        success, color = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            # eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            # faces=detector.detectMultiScale(frame,1.1,7)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #  #Draw the rectangle around each face
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #     roi_gray = gray[y:y+h, x:x+w]
            #     roi_color = frame[y:y+h, x:x+w]
            #     eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
            #     for (ex, ey, ew, eh) in eyes:
            #         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # ret, buffer = cv2.imencode('.jpg', frame)
            # frame = buffer.tobytes()
            # yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # _, color = video_capture.read()
            # transform color -> grayscale
            bw = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
            # detect the face and blur it
            blur = find_and_blur(bw, color)

            ret, buffer = cv2.imencode('.jpg', blur)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # display output
            # cv2.imshow('Video', blur)
            # # break if q is pressed
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            # yield blur
def gen_frames_nor():  
    while True:
        success, color = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', color)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed_nor')
def video_feed_nor():
    return Response(gen_frames_nor(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True)