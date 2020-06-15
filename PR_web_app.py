from flask import Flask,render_template,request
import numpy as np
import cv2
import base64
import sys
import json
import PlateRoc


# Define App
app = Flask(__name__,template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')


# Handles uploaded image
@app.route('/upload',methods=["POST"])
def upload():
    try:
        # Get uploaded form
        d = request.form
        # Extract the data field
        data = d.get('data')

        # The first part of the string simply indicates 
        # what kind of file it is. So we extract only the data part. 
        #print(data)
        data = data.split(',')[1]    
        # Get base64 decoded 
        data = base64.decodebytes(data.encode())

        # Convert to numpy array
        nparr = np.frombuffer(data, np.uint8)

        # Read image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #cv2.imwrite("./test.jpg", img)

        #detect Plates
        img, jsn = PlateRoc.detectLicensePlate(img)
        print(jsn)

        # Encode output images
        _, im_arr = cv2.imencode('.jpg', img)  # im_arr: image in Numpy one-dim array format.
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes)
        im_b64 = im_b64.decode('ascii')
        #imgutf8 = im_bytes.decode("utf-8") 
        jsn['Data'] = im_b64
        # Return result as a json object
        return json.dumps(jsn), 200, {'ContentType':'application/json'} 
    except:        
        return json.dumps({'Vehicle_Detected': 0, 'Plates':[]}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,threaded=False)