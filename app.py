from kb import Kaith
from flask import Flask, render_template, request, redirect
from kb import Kaith
import base64
from io import BytesIO
from PIL import Image

kaith = Kaith("http://kaith-service.4a6b1f6298f847ad8268.japaneast.aksapp.io")
table = kaith.table(
    repo_id="1634603081188511745",
    table_id="1634603498353987584",
    field_type="name"
)
app = Flask(__name__)


@app.route('/')
def hello():

    data = table.select()
    print(data[0]['images'].raw)
    return render_template('index.html', records=data[::-1])


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    image = Image.open(file)
    im_file = BytesIO()
    image.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)
    uploader = kaith.uploader()
    resp = uploader.upload(im_b64)
    new_record = table.create({"name": file.filename})
    new_record["image"] = resp["link"]
    new_record.save()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
