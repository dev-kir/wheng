from flask import Flask
from app import routes

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'idontknowwheretogetthersecretkeyatall'

app.register_blueprint(routes.main)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
