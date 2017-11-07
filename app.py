from flask import Flask, render_template, request
import cv2
import numpy
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        img = cv2.pyrDown(cv2.imread(f.filename, cv2.IMREAD_UNCHANGED))
        # threshold image
        ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 245, 255, cv2.THRESH_BINARY)
        totalPixel = threshed_img.size
        whitePixel = cv2.countNonZero(threshed_img)
        restar = whitePixel / totalPixel * 100
        print(restar)
        print(100 - restar)
        proporcion = (100 - restar)
        resultado = 602.64 * (proporcion / 100)
        return render_template("results.html", resultado=resultado)


if __name__ == '__main__':
    app.run()