from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        resultado = "hola Gera"
        return render_template("results.html", resultado=resultado)


if __name__ == '__main__':
    app.run(debug = True)