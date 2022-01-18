from flask import *

admin_signin = Blueprint(
    "admin_signin", 
    __name__, 
    template_folder="templates/admin"
)

@admin_signin.route("/member")
def member():
    if "email" in session: 
        successSignIn = request.args.get("successSignIn", "")
        return render_template("member.html", successSignIn = successSignIn)
    else:
        return redirect('/')

@admin_signin.route("/error")
def error():
    msg = request.args.get("msg", "發生錯誤，聯繫客服")
    return render_template("error.html", msg = msg)

@admin_signin.route('/processing', methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]

    if email == "test": # 登入成功
        if password == "test":
            #  建立 session 保存資料
            session["email"] = email
            return redirect("/signin/member?successSignIn=恭喜您，成功登入系統")
        else: # 登入失敗
            return redirect("/signin/error?msg=帳號密碼輸入錯誤") 
    else: # 登入失敗
        return redirect("/signin/error?msg=帳號密碼輸入錯誤") 
