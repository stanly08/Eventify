from flask import render_template
from app import app, db
from app.models import Event

@app.route('/')
@app.route('/index')
def index():
    events = Event.query.all()
    return render_template('event_list.html', events=events)
