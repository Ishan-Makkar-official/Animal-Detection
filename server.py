from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
from flask_cors import CORS, cross_origin
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
import numpy as np
import cv2
import base64

app = Flask(__name__)        

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# POST - just get the image and metadata
@app.route('/predict', methods=['POST'])
@cross_origin()
def post():
    # r=request()
    # print(r)
    # request_data = request.form['some_text']
    # print(request_data)
    imagefile = request.files.get('image', '')
    #print(imagefile)
    # plt.imshow(imagefile)
    #print("hello",imagefile)
    imagefile.save('./test_image.jpg')
    img = cv2.imread('./test_image.jpg')
    print(img)
    image_resize=cv2.resize(img,(256,256))
    image_resize = np.expand_dims(image_resize, axis=0)
    y=new_model.predict(image_resize)
    y=y.T
    output="Wild"
    if y[2]>y[0] and y[2]>y[1]:
        output='Wild'
    else :
        output='Not Wild'
    return jsonify({'output':output})

if __name__=='__main__':
    new_model=tf.keras.models.load_model('./Saved_Model')
    app.run(port=5000)