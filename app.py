from flask import Flask, request, send_file, render_template
import barcode
from barcode.writer import ImageWriter
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')

    code128 = barcode.get_barcode_class('code128')
    barcode_obj = code128(text, writer=ImageWriter())

    buffer = io.BytesIO()
    barcode_obj.write(buffer)
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)