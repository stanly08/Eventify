from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from .models import Event
from .forms import EventForm
from . import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('Access denied.', 'danger')
        return redirect(url_for('user.dashboard'))
    return render_template('admin_dashboard.html', user=current_user)

@admin_bp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    if not current_user.is_admin:
        flash('Access denied.', 'danger')
        return redirect(url_for('user.dashboard'))
    
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            image=form.image.data,  # Make sure this handles the file upload properly
            # Add other fields as necessary
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('admin.dashboard'))
    return render_template('create_event.html', form=form)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out as admin.', 'success')
    return redirect(url_for('main.home'))

