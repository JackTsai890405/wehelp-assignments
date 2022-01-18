from flask import *
from admin.signin import admin_signin
from admin.signout import admin_signout

app = Flask(
	__name__, # 建立 Application 物件
	static_folder = "static/images",
	static_url_path = "/static/images"
)

app.secret_key = 'any string but secret'

app.register_blueprint(admin_signin, url_prefix="/signin")
app.register_blueprint(admin_signout, url_prefix="/signout")

@app.route("/")
def test():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)