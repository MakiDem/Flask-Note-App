from flask import Blueprint, flash, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  if request.method == 'POST':
    note = request.form.get('note')
    if note:
      new_note = Note(data=note, user_id=current_user.id)
      db.session.add(new_note)
      db.session.commit()
      flash('Note added successfully!', category='success')
    else:
      flash('Note cannot be empty.', category='danger')

  return render_template('home.html', user=current_user)
  