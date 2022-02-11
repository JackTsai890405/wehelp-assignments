from flask import *

# 功能
from admin.signin import admin_signin
from admin.signup import admin_signup
from admin.signout import admin_signout

app = Flask(
    __name__,
    static_folder = "/static/images",
    static_url_path = "/static/images"
)

app.secret_key = "any string but secret"

# 註冊 Flask Blueprints
# app.register_blueprint(admin_signin, url_prefix = "/signin")
# app.register_blueprint(admin_signup, url_prefix = "/signup")
# app.register_blueprint(admin_signout, url_prefix = "/signout")
app.register_blueprint(admin_signin)
app.register_blueprint(admin_signup)
app.register_blueprint(admin_signout)

@app.route("/")
def index(): 
    return render_template("index.html")

if __name__ == "__main__": 
    app.run(debug=True)