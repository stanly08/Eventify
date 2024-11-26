from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from app.models import User, Event

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password.')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('login.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(username=username).first() is not None:
            flash('Username already exists.')
            return redirect(url_for('main.signup'))
        if User.query.filter_by(email=email).first() is not None:
            flash('Email already exists.')
            return redirect(url_for('main.signup'))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully.')
        return redirect(url_for('main.login'))
    return render_template('signup.html')

@main.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@main.route('/register_event/<int:event_id>', methods=['POST'])
@login_required
def register_event(event_id):
    flash('You have successfully registered for the event!')
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

