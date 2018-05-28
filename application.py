from flask import Flask, request, send_file, Response, make_response
from zatiq_food_images_client import ZatiqFoodImagesClient

application = Flask(__name__)

zatiq_images = ZatiqFoodImagesClient()

@application.route('/')
def test_server_online():
    return("Server is online")

@application.route('/upload/', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        jsonData = request.form['imagedata']
        if jsonData == None:
            return('No image provided to upload', 400)
        else:
            imagedata = jsonData
            try:
                response = zatiq_images.save_image_locally(imagedata)
            except Exception as e:
                return("Error \n %s" % (e))
        json_response = Response(response=make_response(response), status=200, mimetype='application/json')
        print(json_response)
        return(json_response)

@application.route('/delete/', methods=['POST'])
def delete_image():
    if request.method == 'POST':
        jsonData = request.form['imagepath']
        if jsonData == None:
            return('No image path provided to delete', 400)
        else:
            imagepath = jsonData
            try:
                response = zatiq_images.delete_local_image(imagepath)
            except Exception as e:
                return("Error \n %s" % (e))
        return Response(response=make_response(response), status=200, mimetype='application/json')

@application.route('/image/<imagepath>', methods=['GET'])
def get_image(imagepath):
    if request.method == 'POST':
        jsonData = request.get_json()
        if 'imagepath' not in jsonData:
            return('No image path provided to GET', 400)
        else:
            imagepath = jsonData['imagepath']
            return(send_file('./images'+imagepath, mimetype='image/png'))

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=5000)