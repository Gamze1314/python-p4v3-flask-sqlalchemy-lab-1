# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
# route /earthquakes/<int:id>
# get the earthquake with that id, and return a response containing the valuesformatted as JSON string. if no row found, return error message.
# status is 200


@app.route('/earthquakes/<int:id>')
def get_magnitude_by_id(id):

    # query the db
    magnitude = Earthquake.query.filter_by(id=id).first()

    if magnitude:  # if magnitude is found with given id
        body = magnitude.to_dict() # convert it to dictionary
        status = 200
    else:
        body = {'message': f'Earthquake {id} not found.'}
        status = 404

    return make_response(body, status)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
