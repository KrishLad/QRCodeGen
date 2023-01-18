from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__) #initializes Flask

@app.route('/')
def home():
    """ This is the homepage of the website
    """
    return  render_template('index.html')


@app.route('/', methods=['POST'])
def generateQR():
    """ Grabs the link user inputted and returns a QR code version
    """
    mem = BytesIO() #init BytesIO
    data = request.form.get('link') #grabs link from 
    img = qrcode.make(data) #makes qrcode
    img.save(mem)
    mem.seek(0) #read data from begninning 

    base64 = 'data:image/png;base64,' + b64encode(mem.getvalue()).decode('ascii') #turns into base 64

    return render_template('index.html', data=base64)

#start server
if __name__ == '__main__':
    app.run(debug=True)