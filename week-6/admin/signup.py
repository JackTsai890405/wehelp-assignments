from crypt import methods
from multiprocessing import connection
from flask import *
import mysql.connector
from numpy import record

admin_signup = Blueprint(
    "admin_signup", 
    __name__, 
    template_folder = "/templates/admin"
)

# /error ( 註冊失敗 )
@admin_signup.route("/error", methods=["GET"])
def error():
    errorMessage = request.args.get("errorMessage", "")
    return render_template("error.html", errorMessage = errorMessage)

# /signup ( 處理中 )
@admin_signup.route('/signup', methods=["POST"])
def signup():
    connection = mysql.connector.connect(
        host = "localhost", 
        port = "3306", 
        user = "root", 
        password = "root1234", 
        database = "L1_W6"
    )
    cursor = connection.cursor()
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    query_member = ("SELECT * FROM `member` "
                    "WHERE `username` = %s")

    query_data = (username, )

    cursor.execute(query_member, query_data)
    # 資料回傳是 list 包 tuple
    records = cursor.fetchall()

    # /signup/error
    if len(records) > 0: 
        cursor.close()
        connection.close()
        return redirect("/error?errorMessage=帳號已經被註冊")
    # / : 註冊成功，導回首頁網址
    elif (len(name) > 0) and (len(username) > 0) and (len(password) > 0): # 首次註冊，且資料填寫正確
        session["username"] = username
        add_member = ("INSERT INTO `member` (`name`, `username`, `password`) VALUES (%s, %s, %s)")
        data_member = (name, username, password)
        cursor.execute(add_member, data_member)
        connection.commit()
        cursor.close()
        connection.close()
        return redirect("/")