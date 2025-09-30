from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"New Message: {name} | {email} | {message}")  
        return redirect(url_for("home")) 
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
