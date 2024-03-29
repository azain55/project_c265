import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)

 
@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))


# Code for Project 265 Grayscale start here
   def upload_video(filename):

       sorve = cv2.VideoCapture(f'static/' + filename)
       frame_height = int(sorce.get(4))
       frame_width = int(sorce.get(3))
       size = (frame_width, frame_height)


       return sorce

def cv2.VideoWriter():
    folder_name = 'static/' + 'blackandwhite.mp4'
    folder_name += ','





















   
            
# Code for Project 265 end here

    return render_template('upload.html', filename=filename)



# Code for Project 265 download funcion starts here







# Code for Project 265 download funcion ends here



@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run(debug=True)
