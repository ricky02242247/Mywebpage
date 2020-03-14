import os
import glob
from flask import Flask, render_template
server = Flask("Ricky")

@server.route("/")
def index():
    ds = glob.glob("website/*")
    ds = [d.split("/")[-1] for d in ds]
    return render_template("index.html",dirs=ds)

@server.route("/page/<c>")
def diary(c):
    fs = glob.glob("website/"+ c + "/*.txt")
    contents = []
    for i ,fn in enumerate(fs):
        name = os.path.split(fn)[-1].replace(".txt", "")
        f = open(fn)
        page = f.read()
        f.close()
        contents.append((name, page, i))
    return render_template("page.html", cs = contents)

server.run(debug=True,
           host="0.0.0.0",
           port="3000")