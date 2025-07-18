from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<h1>Logout Page</h1>'

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 8:
            flash('Email cannot be less than 8 characters.', category='danger')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        elif password1 != password2:
            flash("Passwords don't match.", category='danger')
        else:
            flash('Account created successfully', category='success')

    return render_template('signup.html')