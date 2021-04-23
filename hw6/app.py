from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.flats import flat_app
from models.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@hw6_db/hw6'
app.register_blueprint(flat_app, url_prefix="/flats")

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
