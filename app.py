from flask import Flask, flash, request, redirect, send_file, url_for, render_template
from modules import convert_to_grayscale, blur_image, sharpen_image ,contrast_image,transpose_image, convert_to_colour #importing all the functions from blur.py
from modules import rot_image,mirror_image,bright_image,saturation_image, shear_imageX, shear_imageY, sketch_image, rescale_image
import os

app = Flask(__name__)  
app.secret_key = "secret key"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

#route to home
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

#route to gray scale function
@app.route('/saturation', methods=['POST'])
def saturation():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        val=request.form['value']
        saturation_img = saturation_image(file,val)
        return send_file(saturation_img, mimetype='image/PNG')

@app.route('/grayscale', methods=['POST'])
def grayscale():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        grayscale_img = convert_to_grayscale(file)
        return send_file(grayscale_img, mimetype='image/PNG')

@app.route('/blur', methods=['POST'])
def blur():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        blurred_img = blur_image(file)
        return send_file(blurred_img, mimetype='image/PNG')

@app.route('/sharpen', methods=['POST'])
def sharpen():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        val=request.form['value']
        sharpen_img = sharpen_image(file,val)
        return send_file(sharpen_img, mimetype='image/PNG')

@app.route('/contrast', methods=['POST'])
def contrast():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        val=request.form['value']
        contrast_img = contrast_image(file,val)
        return send_file(contrast_img, mimetype='image/PNG')



@app.route('/color', methods=['POST'])
def color():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        color_img = convert_to_colour(file)
        return send_file(color_img, mimetype='image/PNG')

@app.route('/rescale', methods=['POST'])
def rescale():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        rescale_img = rescale_image(file)
        return send_file(rescale_img, mimetype='image/PNG')

@app.route('/shearX', methods=['POST'])
def shearX():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        shear_img = shear_imageX(file)
        return send_file(shear_img, mimetype='image/PNG')

@app.route('/shearY', methods=['POST'])
def shearY():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        shear_img = shear_imageY(file)
        return send_file(shear_img, mimetype='image/PNG')

@app.route('/sketch', methods=['POST'])
def sketch():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        sketch_img = sketch_image(file)
        return send_file(sketch_img, mimetype='image/PNG')


@app.route('/transpose', methods=['POST'])
def transpose():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        transpose_img = transpose_image(file)
        return send_file(transpose_img, mimetype='image/PNG')

@app.route('/mirror', methods=['POST'])
def mirror():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        mirror_img = mirror_image(file)
        return send_file(mirror_img, mimetype='image/PNG')

@app.route('/bright', methods=['POST'])
def bright():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        val=request.form['value']
        bright_img = bright_image(file,val)
        return send_file(bright_img, mimetype='image/PNG')



@app.route('/rot', methods=['POST'])
def rot():
    if 'file' not in request.files:
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        rot_img = rot_image(file)
        return send_file(rot_img, mimetype='image/PNG')

if __name__ == "__main__":
    app.debug='true'
    app.run(port=5000,debug=True)