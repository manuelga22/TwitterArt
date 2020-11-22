import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import requests

import os
import sys
from PIL import Image
# from deepface import DeepFace

#importing all dependencies
import numpy as np
import tweepy 
import pandas as pd
from flask_cors import CORS
import  io, base64
from os import environ 

#app = Flask(__name__)
CORS(app)
#variables for accessing twitter API
consumer_key='swzpmLwhOjAicnxkK0B85jot5'
consumer_secret_key='HHTb1U7x1VaQtOla5MLftHfaZLscNsM8udAvJWoWGbuogMA4Lb'
access_token='1054798969447034880-U5regDkOohLSybJ3qVedUsctrGdjTQ'
access_token_secret='TQv7TGscDUrkglpSYwE0eXWgT6Gy7faC06He4yNQu1D2V'



#CORS(app, resources={r"/*": {"origins": "*"}})

def compressMe(folder, file):
    picture = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], file))
    picture.save(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + file),
                 "JPEG",
                 optimize=True,
                 quality=15)
    return True


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed')
        return render_template('index.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/style', methods=['POST'])
def style_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if request.form.get("mosaic"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=mosaic"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename) )

            # filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename)


            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_Mosaic_" +filename))
        if request.form.get("udnie"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=udnie"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" + filename)):
                return render_template('show_image.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" +filename))

            # print("Hello")
            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_udnie_" +filename))
        if request.form.get("candy"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=candy"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" +filename))

            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_candy_" +filename))
        if request.form.get("rain_princess"):
            compressMe(app.config['UPLOAD_FOLDER'], filename)
            files = {'image': open(os.path.join(app.config['UPLOAD_FOLDER'], "Compressed_" + filename), 'rb')}

            url = "http://max-fast-neural-style-transfer.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud/model/predict?model=rain_princess"

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" + filename)):
                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" +filename))

            response = requests.post(url, files=files,verify=False)

            if response.status_code == 200:
                with open(os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" + filename), 'wb') as f:
                    f.write(response.content)

                return render_template('show_image.html',  filename=os.path.join(app.config['UPLOAD_FOLDER'], "Style_rain_princess_" +filename) )
        # else:
        #     try:
        #         # print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         # obj = DeepFace.analyze(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         # print(obj)
        #         # obj['age']=int(obj['age'])

        #         # print(filename)

        #         return render_template('show_image.html', age=obj['age'],dominant_emotion=obj['dominant_emotion'],dominant_race=obj['dominant_race'],gender=obj['gender'],filename=os.path.join(app.config['UPLOAD_FOLDER'],  filename))



            # except Exception as e:
            #     print("In except ")
            #     print(e)


        return render_template('show_image.html', filename=os.path.join(app.config['UPLOAD_FOLDER'], filename))

    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

    # do something


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/tweet', methods=['POST'])
def tweet():
    data= request.form['picture']
    im = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1])))
    filename = "newPicture.jpeg"
    im.save("static/uploads/"+filename)
    twitter_auth_keys = { 
        "consumer_key"        : consumer_key,
        "consumer_secret"     : consumer_secret_key,
        "access_token"        : access_token,
        "access_token_secret" : access_token_secret
    }
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
    #the image needs to be stored and the path has to be here! 
    media = api.media_upload("./static/uploads/"+filename)
    tweet = "THANK YOU CODECHELLA #Codechella"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)

    # app.run(debug=True)