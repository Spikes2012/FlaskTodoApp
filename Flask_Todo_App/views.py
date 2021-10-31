from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def hello():
    return render_template("login.html")

@views.route("/index")
def index():
    return render_template("index.html")


# @views.route('/task_page')
# def tasks():
#     return render_template("task_page.html")


@views.route('/wiki')
def wiki():
    return render_template("wiki.html")


@views.route("/home")
def redirectPage():
    return redirect(url_for("views.hello"))