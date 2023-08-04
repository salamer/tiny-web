from flask import Flask, jsonify, render_template
from leapcell import Leapcell

client = Leapcell(
    "xxx",
)

table = client.table(
    "test1/myblog",
    "1687402598478176256",
    "name",
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    pages = [{
        "id": page.record_id,
        "title": page["name"],
        "content": page["content"],
        "tag": page["tag"],
        "cover": page["cover"][0] if page["cover"] else "",
    } for page in table.select().offset(0).query()]

    return render_template("index.html", blogs=pages)


@app.route("/blog/<page>")
def page(page: str):
    page = table.get_by_id(page)
    blog = {
        "id": page.record_id,
        "title": page["name"],
        "content": page["content"],
        "tag": page["tag"],
        "cover": page["cover"][0] if page["cover"] else "",
    }
    return render_template("page.html", blog=blog)


@app.route("/label/<label>")
def label(label: str):
    pages = [{
        "id": page.record_id,
        "title": page["name"],
        "content": page["content"],
        "tag": page["tag"],
        "cover": page["cover"][0] if page["cover"] else "",
    } for page in table.select().where(table['tag'].contain(label)).offset(0).query()]
    return render_template("index.html", blogs=pages)


if __name__ == '__main__':
    app.run()
