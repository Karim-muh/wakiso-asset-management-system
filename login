pip install flask-login werkzeug
from flask import request, render_template, redirect
from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect('/dashboard')
    
    return render_template('login.html')
from functools import wraps

def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get('role') != 'admin':
            return "Access Denied"
        return f(*args, **kwargs)
    return wrapper
