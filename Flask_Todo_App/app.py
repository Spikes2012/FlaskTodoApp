from flask import Flask
from views import views
from auth import auth
from task_page import tasks

# from flask_login

app = Flask(__name__)

app.secret_key = '1234567'


app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(tasks,url_prefix="/")


# @app.route('/home/<string:name>', methods=['GET'])
# def helloName(name):
#     return "hello, " + name


if __name__ == "__main__":
    app.run(debug=True)
