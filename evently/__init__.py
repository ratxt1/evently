from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from evently.models import db, connect_db
from secrets import SECRET_KEY


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///evently'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = SECRET_KEY


connect_db(app)
# db.create_all()

debug = DebugToolbarExtension(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


#copy this pattern for additional blueprints
from evently.views import general
app.register_blueprint(general.mod)
