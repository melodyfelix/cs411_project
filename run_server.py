from flask import Flask
from views.routes import index_blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = ""
db.init_app(app)
app.register_blueprint(index_blueprint)
app.run(debug=True)