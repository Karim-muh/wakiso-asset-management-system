from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="asset_db"
)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/assets')
def assets():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM assets")
    data = cursor.fetchall()
    return render_template('assets.html', assets=data)

@app.route('/add_asset', methods=['POST'])
def add_asset():
    name = request.form['name']
    category = request.form['category']

    cursor = db.cursor()
    cursor.execute("INSERT INTO assets (name, category) VALUES (%s, %s)", (name, category))
    db.commit()

    return redirect('/assets')

app.run(debug=True)
