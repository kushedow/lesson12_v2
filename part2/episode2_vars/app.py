import json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ----------
# DEMOS
# ----------

@app.route('/demo2')
def demo2():
    return render_template("index.html", name="John", surname="Doe", skill="Python")



if __name__ == '__main__':
    app.run(debug=True)
