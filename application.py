from flask import Flask, request, send_from_directory
import json
import sys
import logging
from zatiq_food_images_client import ZatiqFoodImagesClient

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='./app.log', filemode='w')

application = Flask(__name__, static_url_path='')

zatiq_images = ZatiqFoodImagesClient()

@application.route('/')
def test_server_online():
    return("Server is online")

@application.route('/upload/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        jsonData = request.get_json()
        if not jsonData['imagedata']:
            return('No image provided to upload', 400)
        else:
            imagedata = jsonData['imagedata']
            try:
                response = zatiq_images.save_image_locally(imagedata)
            except Exception as e:
                return("Error \n %s" % (e))
        return(response)

@application.route('/update/', methods=['POST'])
def update_image():
    if request.method == 'POST':
        jsonData = request.get_json()
        if not (jsonData['imagedata'] and jsonData['imagepath']):
            return('Invalid request', 400)
        else:
            imagedata = jsonData['imagedata']
            imagepath = jsonData['imagepath']
            
            if zatiq_images.delete_local_image(imagepath) == 'TRUE':
                response = zatiq_images.save_image_locally(imagedata)
            else:
                return "No such image found to update"
        return(response)

@application.route('/delete/', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        jsonData = request.get_json()
        if not jsonData['imagepath']:
            return('No image path provided to delete', 400)
        else:
            imagepath = jsonData['imagepath']
            try:
                response = zatiq_images.delete_local_image(imagepath)
            except Exception as e:
                return("Error \n %s" % (e))
        return(response)

@application.route('/image/<imagepath>')
def get_image(imagepath):
        return(send_from_directory(directory='images', filename=imagepath))

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)