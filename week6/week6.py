import mysql.connector #連線到資料庫
con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="website"
)

print("資料連線成功")

#關閉資料庫
con.close()
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"
#處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "username" in session:
        username = session["username"]
        con = mysql.connector.connect(
                    user='root',
                    password='12345678',
                    host='localhost',
                    database='website'
                )

        cursor = con.cursor()
        cursor.execute("SELECT name from member WHERE username = %s", (username,))
        name = cursor.fetchone()
        cursor.execute("SELECT name, content FROM `member` INNER JOIN message ON `member`.id=message.member_id;")
        message = cursor.fetchall()

        messages=[]

        for messageName, content in message:
                displayMessage = f"{messageName}: {content}"
                messages.append(displayMessage)

        if name:
            name = name[0]
            return render_template("member.html", member_name=name, messages=messages)
        else:
            con.close()
            return redirect("/")
    else:
        return redirect("/")
    

#/error?message=錯誤訊息
@app.route("/error")
def error():
    msg=request.args.get("message","發生錯誤請聯繫客服")
    return render_template("error.html", msg=msg)

@app.route("/signin",methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]

    con = mysql.connector.connect(
        user="root",
        password="12345678",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    check_user_sql = "SELECT id, name FROM member WHERE username = %s AND password = %s"
    cursor.execute(check_user_sql, (username, password))
    user = cursor.fetchone()

    if user:
        session["username"] = username
        return redirect("/member")
   
    else:
        con.close()
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/signout",methods=["GET"])
def signout():
    del session["username"]
    return redirect("/")

@app.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
   
    con = mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="website"
        )
    cursor = con.cursor()
    check_duplicate_sql = "SELECT username FROM member WHERE username = %s"
    cursor.execute(check_duplicate_sql, (username,))
    existing_username = cursor.fetchone()

    if existing_username:
        cursor.close()
        con.close()
        return redirect("/error?message=帳號已經被註冊")

    sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    values = (name, username, password)
    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()
    
    return redirect("/")


@app.route("/createMessage", methods=["POST"])
def createMessage():
    if "username" in session:
        username = session["username"]
        content = request.form["content"]

        
        con = mysql.connector.connect(
                user='root',
                password='12345678',
                host='localhost',
                database='website'
            )

        cursor = con.cursor()
        cursor.execute("SELECT id from `member` WHERE username = %s", (username,))
        exist_id = cursor.fetchone()

        if exist_id:
            exist_id = exist_id[0]
            cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (exist_id, content))
            con.commit()
            return redirect("/member")


    return redirect("/member")

app.run(port=3000)