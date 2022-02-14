from flask import *
import mysql.connector
from numpy import record

admin_api = Blueprint (
    "admin_api", 
    __name__, 
    template_folder = "/templates/admin"
)

@admin_api.route("/members", methods=["GET"])
def queryMember(): 
    username = request.args.get("username", "")
    
    connection = mysql.connector.connect(
        host = "localhost", 
        port = "3306", 
        user = "root", 
        password = "root1234", 
        database = "L1_W6"
    )
    cursor = connection.cursor()

    # 查詢會員資料
    query_member = ("SELECT * FROM `member` "
                    "WHERE `name` = %s")
    query_data = (username, )
    cursor.execute(query_member, query_data)

    # 資料回傳是 list 包 tuple
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    if len(records) > 0: 
        output = {
            "id": records[0][0],
            "name": records[0][1],
            "username": records[0][2]
        }
        # return {"data": output}
        return jsonify({"data": output})
    else:
        return jsonify({"data": None})

@admin_api.route("/member", methods=["POST"])
def updateMember(): 
    username = request.get_json()
    print(username["name"])

    connection = mysql.connector.connect(
        host = "localhost", 
        port = "3306", 
        user = "root", 
        password = "root1234", 
        database = "L1_W6"
    )
    cursor = connection.cursor()

    # 查詢會員資料
    update_member = ("UPDATE `member` "
                    "SET `name` = %s "
                    "WHERE `username` = %s")
    update_data = (username["name"], session["username"])
    cursor.execute(update_member, update_data)

    connection.commit()
    # 成功
    return jsonify({"ok": True})
    # 失敗
    return jsonify({"error": True})
