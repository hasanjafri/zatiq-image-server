from flask import Flask, request, send_file
from zatiq_food_images_client import ZatiqFoodImagesClient

application = Flask(__name__)

zatiq_images = ZatiqFoodImagesClient()

@application.route('/upload/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        jsonData = request.get_json()
        if 'imagedata' not in jsonData:
            return('No image provided to upload', 400)
        else:
            imagedata = jsonData['imagedata']
            try:
                response = zatiq_images.save_image_locally(imagedata)
            except Exception as e:
                return("Error \n %s" % (e))
            return(response)

@application.route('/delete/', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        jsonData = request.get_json()
        if 'imagepath' not in jsonData:
            return('No image path provided to delete', 400)
        else:
            imagepath = jsonData['imagepath']
            try:
                response = zatiq_images.delete_local_image(imagepath)
            except Exception as e:
                return("Error \n %s" % (e))
            return(response)

@application.route('/image/<imagepath>', methods=['GET'])
def get_image(imagepath):
    if request.method == 'POST':
        jsonData = request.get_json()
        if 'imagepath' not in jsonData:
            return('No image path provided to GET', 400)
        else:
            imagepath = jsonData['imagepath']
            return(send_file('./images'+imagepath, mimetype='image/png'))