from flask import render_template
from app import app, db
from app.models import Event

@app.route('/user/dashboard')
def user_dashboard():
    events = Event.query.all()
    return render_template('user_dashboard.html', events=events)

@app.route('/events')
def event_list():
    events = Event.query.all()
    return render_template('event_list.html', events=events)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@app.route('/register_event/<int:event_id>', methods=['POST'])
def register_event(event_id):
    # Handle event registration logic here
    flash('You have successfully registered for the event!')
    return redirect(url_for('event_detail', event_id=event_id))
