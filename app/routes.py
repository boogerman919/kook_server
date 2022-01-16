from app import app, db
from app.models import Ride, User

@app.route('/')
@app.route('/starttime/<user_id>', methods=['GET'])
def index(user_id):
    # get the last ride of the user from the database
    r = User.query.get(user_id).rides[-1]
    return {"id": r.id, "start_time": str(r.start_time)}