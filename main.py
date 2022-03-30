from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/form")
@app.route("/form", methods=["POST"])
def form():

    if request.method == "POST":
        return render_template('form.html', error="post")

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
