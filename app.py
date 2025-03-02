from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="",  # Change this to your MySQL password
    database="fitness_coaching"
)
cursor = db.cursor()

# 🏠 Home Page
@app.route("/")
def home():
    if "user" in session:
        return render_template("index.html", username=session["user"])
    return redirect("/login")

# 📝 Registration Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        goal = request.form["goal"]
        password = request.form["password"]
        
        cursor.execute("INSERT INTO users (name, age, gender, goal, password) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, gender, goal, password))
        db.commit()
        
        return redirect("/login")
    
    return render_template("register.html")

# 🔑 Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        
        if user:
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials, try again."
    
    return render_template("login.html")

# 🚪 Logout Functionality
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/exit")

# 🏁 Exit Page
@app.route("/exit")
def exit_page():
    return render_template("exit.html")

if __name__ == "__main__":
    app.run(debug=True)
