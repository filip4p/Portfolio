from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/1")
def open_first_jpg():
    return send_file(path_or_file='static/img/Podajnik wibracyjny.png', as_attachment=False)


@app.route("/2")
def open_2_jpg():
    return send_file(path_or_file='static/img/Podajnikregulowany.png', as_attachment=False)


@app.route("/3")
def open_3_jpg():
    return send_file(path_or_file='static/img/Separator.png', as_attachment=False)


@app.route("/4")
def open_4_jpg():
    return send_file(path_or_file='static/img/Stólzezrztem.png', as_attachment=False)


@app.route("/5")
def open_5_jpg():
    return send_file(path_or_file='static/img/Łuparka2.png', as_attachment=False)


@app.route("/6")
def open_6_jpg():
    return send_file(path_or_file='static/img/LAMPKA.png', as_attachment=False)


@app.route("/7")
def open_7_jpg():
    return send_file(path_or_file='static/img/Kershaw shuffle v4.png', as_attachment=False)


@app.route("/8")
def open_8_jpg():
    return send_file(path_or_file='static/img/CAM.jpg', as_attachment=False)


@app.route("/10")
def open_10_jpg():
    return send_file(path_or_file='static/img/Podajnik wibr.png', as_attachment=False)


@app.route("/download_cv")
def download_cv():
    return send_file(path_or_file='static/img/CV Prorok Filip.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
