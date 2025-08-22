from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Incident, User
from . import db
from .utils import send_email

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    if current_user.role == 'admin':
        incidents = Incident.query.all()
    else:
        incidents = Incident.query.filter_by(created_by=current_user.id)
    return render_template('dashboard.html', incidents=incidents)

@main.route('/incident/new', methods=['GET', 'POST'])
@login_required
def create_incident():
    if request.method == 'POST':
        incident = Incident(
            title=request.form['title'],
            description=request.form['description'],
            created_by=current_user.id
        )
        db.session.add(incident)
        db.session.commit()
        send_email("New Incident Logged", [current_user.email], f"Incident: {incident.title}")
        flash("Incident created")
        return redirect(url_for('main.dashboard'))
    return render_template('incident_form.html')

@main.route('/incident/<int:id>', methods=['GET', 'POST'])
@login_required
def view_incident(id):
    incident = Incident.query.get_or_404(id)
    users = User.query.all()
    if request.method == 'POST' and current_user.role == 'admin':
        incident.status = request.form['status']
        incident.assigned_to = request.form.get('assigned_to')
        db.session.commit()
        send_email("Incident Updated", [incident.created_by.email], f"Status: {incident.status}")
        flash("Incident updated")
    return render_template('incident_list.html', incident=incident, users=users)
