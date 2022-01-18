from flask import *

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")

@second.route("/base")
def base():
    return render_template("base.html")
