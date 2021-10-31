from flask import Blueprint, render_template, redirect, url_for, request, flash
from library import pnpdb as dataBase

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    dataBase.initialize("0001", "admin")
    # dataBase.find_data(email,password)

    return render_template("login.html")

# @auth.route("/logout")
# def logout():
#     return render_template("index.html")


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    data = request.form
    print(data)

    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(fullName) < 2:
            flash('Full Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords are not matching', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            flash('User Created', category='success')

    return render_template("signup.html")
