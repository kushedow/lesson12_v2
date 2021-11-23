import json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/demo3')
def demo3():
    return render_template("index.html", age=18, img_url="http://via.placeholder.com/150x150")



if __name__ == '__main__':
    app.run(debug=True)
