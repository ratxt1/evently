from flask import Blueprint
from evently.models import db_session

mod = Blueprint('general', __name__)

## Example syntax:

# @mod.route('/')
# def homepage():
#     return render_template('general/homepage.html')

