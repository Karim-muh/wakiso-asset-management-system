from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Optional
import mysql.connector
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
csrf = CSRFProtect(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="asset_db"
)


class AssetForm(FlaskForm):
    name = StringField('Asset Name', validators=[DataRequired(), Length(max=20)])
    category = StringField('Category', validators=[Optional(), Length(max=50)])
    location = StringField('Location', validators=[Optional(), Length(max=20)])


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/assets')
def assets():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM assets")
    data = cursor.fetchall()
    return render_template('assets.html', assets=data)


@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    form = AssetForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data or None
        location = form.location.data or None

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO assets (name, category, location) VALUES (%s, %s, %s)",
            (name, category, location),
        )
        db.commit()
        flash('Asset added successfully.', 'success')
        return redirect(url_for('assets'))

    return render_template('add_asset.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
