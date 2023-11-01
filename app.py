from flask import Flask, render_template, request
from extract_aadhar import extract_aadhar_number

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = f"{app.config['UPLOAD_FOLDER']}/{uploaded_file.filename}"
        uploaded_file.save(file_path)
        aadhar_numbers = extract_aadhar_number(file_path)
        aadhar_numbers = [num for num in aadhar_numbers if 1000 <= int(num) <= 9999 and int(int(num)/1000) != 2]
        result = f"Extracted Aadhar Numbers: {' '.join(aadhar_numbers)}"
    else:
        result = "No file uploaded"

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
