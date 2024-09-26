from flask import Flask, render_template, request, redirect, url_for, flash, session
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
    
@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form.get('textbox')
        processed_text = text.upper()
        f = open("data.txt", 'w')
        f.write(processed_text)
        f.close()
    if request.method == 'GET':
        f = open("dats.txt", 'r')
        text=f.read()
        f.close()
    return render_template("my-form.html", text=text)


if __name__ == '__main__':
    app.run()
