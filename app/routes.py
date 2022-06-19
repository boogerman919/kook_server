from urllib import response
from app import app, db
from app.models import ContactMessage, Ride, User
from flask import request, make_response, jsonify
from datetime import datetime

@app.route('/')

@app.route('/start_ride', methods=['POST'])
def start_ride():
    user_id = request.json['user_id']       # TODO: vulnerbility
    board_id = request.json['board_id']

    ride = Ride(user_id=user_id, board_id=board_id)

    db.session.add(ride)
    db.session.commit()
    responseObject = {
        'status': 'success',
        'message': 'Successfully started ride.',
        "ride_id": ride.id,
        "start_time": ride.start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    return make_response(jsonify(responseObject)), 200

@app.route('/end_ride', methods=['POST'])
def end_ride():
    ride_id = request.json['ride_id']

    ride = Ride.query.get(ride_id)

    ride.end_time = datetime.utcnow()

    db.session.commit()

    responseObject = {
        'status': 'success',
        'message': 'Successfully started ride.',
        "start_time": ride.start_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end_time": ride.end_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    return make_response(jsonify(responseObject)), 200

@app.route('/get_rides', methods=['GET'])
def get_rides():
    rides = Ride.query.filter_by(
        user_id=request.args.get('user_id')
    ).order_by(Ride.end_time.desc()).limit(10).all()

    responseObject = []

    for ride in rides:
        print(ride)
        rideObject = {
            "ride_id": ride.id,
            "board_id": ride.board_id,
            "start_time": ride.start_time.strftime("%Y-%m-%dT%H:%M:%SZ") if ride.start_time is not None else None,
            "end_time": ride.end_time.strftime("%Y-%m-%dT%H:%M:%SZ") if ride.end_time is not None else None,
            "cost": ride.cost,
            "beach_name": ride.beach_name,
        }
        responseObject.append(rideObject)

    return make_response(jsonify(responseObject)), 200

@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    message = request.json['message']

    message = ContactMessage(name=name, phone=phone, email=email, message=message)

    db.session.add(message)
    db.session.commit()

    return make_response(jsonify({'status': 'success'})), 200