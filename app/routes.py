from app import app, db
from app.models import Ride, User
from flask import request
from datetime import datetime

@app.route('/')

@app.route('/start_ride', methods=['POST'])
def start_ride():
    user_id = request.json['user_id']
    board_id = request.json['board_id']

    ride = Ride(user_id=user_id, board_id=board_id)

    db.session.add(ride)
    db.session.commit()

    return {"ride_id": ride.id, "start_time": ride.start_time.strftime("%Y-%m-%dT%H:%M:%SZ")}

@app.route('/end_ride', methods=['POST'])
def end_ride():
    ride_id = request.json['ride_id']

    ride = Ride.query.get(ride_id)

    ride.end_time = datetime.utcnow()

    db.session.commit()

    return {"start_time": ride.start_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "end_time": ride.end_time.strftime("%Y-%m-%dT%H:%M:%SZ")}
