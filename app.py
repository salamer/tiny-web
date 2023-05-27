from flask import Flask, render_template, request, redirect
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def hello():
    return {"hello": "world"}

@app.route("/xx")
def xx():
    return {"qq":"xx"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
