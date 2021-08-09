from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_checker():
    horizontal = int(8)
    vertical = int(8)
    startColor = "red"
    secondColor = "black"
    color = ""
    return render_template("checkerboard.html", horizontal = horizontal, vertical = vertical, startColor = startColor, secondColor = secondColor, color = color)

@app.route('/<int:x>')
def horizontal_checker(x):
    horizontal = int(8)
    vertical = int(x)
    startColor = "red"
    secondColor = "black"
    color = ""
    return render_template("checkerboard.html", horizontal = horizontal, vertical = vertical, startColor = startColor, secondColor = secondColor, color = color)

@app.route('/<int:x>/<int:y>')
def dimension_checker(x,y):
    horizontal = int(x)
    vertical = int(y)
    startColor = "red"
    secondColor = "black"
    color = ""
    return render_template("checkerboard.html", horizontal = horizontal, vertical = vertical, startColor = startColor, secondColor = secondColor, color = color)

@app.route('/<int:x>/<int:y>/<startColor>/<secondColor>')
def dimension_color_checker(x,y,startColor,secondColor):
    horizontal = int(x)
    vertical = int(y)
    startColor = startColor
    secondColor = secondColor
    color = ""
    return render_template("checkerboard.html", horizontal = horizontal, vertical = vertical, startColor = startColor, secondColor = secondColor, color = color)

if __name__=="__main__":
    app.run(debug=True)