from flask import request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import app, db
from app.models import Event
import os

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        # Here we will handle the form data
        name = request.form.get('name')
        date = request.form.get('date')
        location = request.form.get('location')
        
        # Here we will handle the file upload
        if 'photo' in request.files:
            file = request.files['photo']
            if file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_event = Event(name=name, date=date, location=location, photo=filename)
            else:
                flash('Invalid file type.')
                return redirect(request.url)
        else:
            flash('No file uploaded.')
            return redirect(request.url)
        
        # Save event details with photo filename in the database
        db.session.add(new_event)
        db.session.commit()
        flash('Event successfully added with photo!')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_dashboard.html')

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)
