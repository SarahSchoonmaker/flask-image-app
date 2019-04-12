import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# home page

@app.route("/")
def index():
    return render_template("upload.html")

# route for rendering the complete.html view given a successful file upload

@app.route("/upload", methods=['POST'])
def upload():

    target = os.path.join(APP_ROOT, 'static/')

    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file=request.files['file']

# if upload isn't blank or a non-jpg or non-png file, then render complete.html. 
# Otherwise stay in the upload.html view and display an error message. 

    if file.filename == '' or file.filename[-3:] != u'jpg' and file.filename[-3:] != u'png':
       return render_template("upload.html", error="Error. Please upload a jpg or png file.")

    for file in request.files.getlist("file"):
     
      filename = file.filename
      destination = "/".join([target, filename])
      file.save(destination)
    
      return render_template("complete.html", image_name=filename)
    
if __name__ == "__main__":
  app.run(port=8080, debug=True)

