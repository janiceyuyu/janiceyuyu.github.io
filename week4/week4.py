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
    if "username" in session and session["username"] == "test":  # 需要檢查 session 中的 username 是否為 "test"
        return render_template("member.html")
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

    if username == "test" and password == "test":
        session["username"]="test"
        return redirect("/member")
   
    elif username == "" or password == "":
        return redirect("/error?message=請輸入完整帳號和密碼")

    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

app.run(port=3000)