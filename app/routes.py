from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from app.models import User, Event
from app.forms import SignupForm, LoginForm, EventForm  # Ensure EventForm is imported

main = Blueprint('main', __name__)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
@main.route('/index')
def index():
    events = Event.query.all()
    return render_template('event_list.html', events=events)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if User.query.filter_by(username=username).first() is not None:
            flash('Username already exists.', 'danger')
            return redirect(url_for('main.signup'))
        if User.query.filter_by(email=email).first() is not None:
            flash('Email already exists.', 'danger')
            return redirect(url_for('main.signup'))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully.', 'success')
        return redirect(url_for('main.login'))
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'danger')
    return render_template('signup.html', form=form)

@main.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main.route('/register_event/<int:event_id>', methods=['POST'])
@login_required
def register_event(event_id):
    flash('You have successfully registered for the event!', 'success')
    return redirect(url_for('main.event_detail', event_id=event_id))

@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@main.route('/user/dashboard')
@login_required
def user_dashboard():
    events = Event.query.all()
    return render_template('user_dashboard.html', events=events)

@main.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            name=form.name.data,
            date=form.date.data,
            location=form.location.data,
            photo=form.photo.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_event.html', form=form)

@main.route('/events')
def event_list():
    events = Event.query.all()
    return render_template('event_list.html', events=events)

