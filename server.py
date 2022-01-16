from app import app, db
from app.models import User, Ride, Board

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Ride': Ride, 'Board': Board}