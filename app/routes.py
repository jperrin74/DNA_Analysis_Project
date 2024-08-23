import os
from flask import render_template, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import DNAForm
from app.models import DNASequence
from app.analyzer import analyze_dna

UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DNAForm()
    if form.validate_on_submit():
        if form.file.data and allowed_file(form.file.data.filename):
            filename = secure_filename(form.file.data.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            form.file.data.save(file_path)
            with open(file_path, 'r') as file:
                sequence = file.read().replace('\n', '')
        else:
            sequence = form.sequence.data

        if sequence:
            analysis_result = analyze_dna(sequence)
            dna_sequence = DNASequence(sequence=sequence, analysis_result=analysis_result)
            db.session.add(dna_sequence)
            db.session.commit()
            flash('DNA sequence analyzed successfully!', 'success')
            return redirect(url_for('report', sequence_id=dna_sequence.id))
        else:
            flash('No DNA sequence provided.', 'danger')
    return render_template('index.html', form=form)

@app.route('/report/<int:sequence_id>')
def report(sequence_id):
    dna_sequence = DNASequence.query.get_or_404(sequence_id)
    return render_template('report.html', dna_sequence=dna_sequence)
