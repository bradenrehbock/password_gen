from flask import Flask, render_template, request, redirect, url_for, session
from password_gen import gen_password
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-here"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_num = "use_num" in request.form

        password = gen_password(length, use_num)
        session["password"] = password

        return redirect(url_for("home"))
    
    password = session.pop("password", "")
    return render_template("index.html", password=password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)