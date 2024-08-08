from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from Pattern_On_PC import count_touching_pixels
from image_generator import create_pixel_art

app = Flask(__name__, template_folder='app/templates')

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'  # New folder for CSV output
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Create upload and output directories if they don't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        new_width = request.form.get('new_width')  # Get the new_width value from the form
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            output_image="static/images/pixel_art.png"
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            csv_filename = filename.rsplit('.', 1)[0] + '.csv'  # Change file extension to .csv
            csv_filepath = os.path.join(app.config['OUTPUT_FOLDER'], csv_filename)
            
            # Check if new_width is provided; if empty, set it to None
            if new_width:
                new_width = int(new_width)
            else:
                new_width = None

            count_touching_pixels(filepath, new_width, output_file=csv_filepath)
            create_pixel_art(csv_filepath, output_image)
            
            return render_template('result.html', result=output_image, result_csv=csv_filename)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_csv(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
