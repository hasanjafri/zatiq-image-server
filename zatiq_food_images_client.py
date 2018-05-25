import secrets
import base64
import os
from pathlib import Path

class ZatiqFoodImagesClient(object):
    def generate_unique_image_name(self):
        image_name = secrets.token_urlsafe(32)
        if self.check_image_name_exists(image_name) == False:
            return(''+image_name+'.png')
        else:
            self.generate_unique_image_name()

    def check_image_name_exists(self, image_name):
        image_path = Path("./images/"+image_name)
        if image_path.is_file():
            return(True)
        else:
            return(False)

    def save_image_locally(self, imagedata):
        if not imagedata:
            return('No image provided')

        file_name = self.generate_unique_image_name()
        with open(file_name, 'wb') as f:
            f.write(base64.decodebytes(imagedata))
        if self.check_image_name_exists(file_name) == True:
            return(file_name)
        else:
            self.save_image_locally(imagedata)

    def delete_local_image(self, imagepath):
        if self.check_image_name_exists(imagepath) == True:
            try:
                os.remove('./images/'+imagepath)
            except Exception as e:
                return("Error \n %s" % (e))

            if self.check_image_name_exists(imagepath) == False:
                return(True)
            else:
                self.delete_local_image(imagepath)