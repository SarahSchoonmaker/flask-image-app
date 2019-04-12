The Image Validator App uploads an image and displays it if the file is a 'jpg' or 'png' file. 

To run the app:
Clone or download the source files. git clone https://github.com/sarahschoonmaker/flask-image-app.git
cd flask-image-app

Create the 'myenv' virtual environment
mkvirtualenv -p flask-image-app/src 

Install required Python packages
cd flask-image-app/src
pip install -r requirements.txt


To run tests, navigate to the src directory and run: python tests/test_basic.py

If you already have Flask and Python installed, CD into the src directory and start the server: python app.py or use the Live Server extension in Visual Studio Code to setup key shortcuts for starting and stopping the server. Navigate to localhost:8080. 

Live Demo: https://my-python-flask-app.herokuapp.com/

 