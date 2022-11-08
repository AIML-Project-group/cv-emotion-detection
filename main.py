from flask import Flask, render_template, request, redirect, send_file
from detector import predict
import cv2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictRoute():
    img = request.files.get('input_image')
    file_name = f'uploads/{img.name}'

    img.save(file_name)

    output = predict(file_name)
    updated_path = file_name + '.' + img.content_type[6:]
    cv2.imwrite(updated_path, output)

    return send_file(updated_path)

app.run(debug=True)
