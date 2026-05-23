from flask import Flask, render_template, request
from password_gen import gen_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        length = int(request.form.get("length"))
        use_num = request.form.get("use_num") == "on"
        password = gen_password(length, use_num)
        return render_template("index.html", password=password)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)