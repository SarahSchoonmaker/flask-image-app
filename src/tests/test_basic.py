import unittest
import requests
import os
from flask import Flask

app = Flask(__name__)

# Creating an instance of the app
class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

# Testing for the home page loading successfully.
    def test_root(self):
        response = self.app.get('/')
        self.assertIn('Validator', response.data)
# Testing for the image upload
    def test_image_upload(self):
        image = self.upload_img()
        response = self.app.post(
            '/upload',
            data=image,
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

# Testing for unacceptable file extensions in the upload process. 
    def test_image_bad_ext(self):
        image = self.upload_img()
        response = self.app.post(
            '/upload',
            data=image,
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)

# Testint that the puppy.jpg file exists. 
    def upload_img(self):
        print(os.getcwd())
        with open('./src/static/puppy.jpg', 'rb') as image:
            return image.read()


unittest.main()