from flask import *

admin_signout = Blueprint(
    "admin_signout", 
    __name__, 
    template_folder="templates/admin"
)

@admin_signout.route("/processing")
def signout():
    # 移除 Session
    del session["email"]
    return redirect("/")
