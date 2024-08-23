from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class DNASequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String(500), nullable=False)
    analysis_result = db.Column(db.String(500), nullable=False)

def analyze_dna(sequence):
    gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    result = f'GC Content: {gc_content:.2f}%'
    if sequence.startswith('ATG'):
        result += ', Start codon found'
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'sequence' in request.form:
            sequence = request.form['sequence']
            analysis_result = analyze_dna(sequence)
            new_sequence = DNASequence(sequence=sequence, analysis_result=analysis_result)
            db.session.add(new_sequence)
            db.session.commit()
            return redirect(url_for('index'))

        if 'file' in request.files:
            file = request.files['file']
            if file:
                sequence = file.read().decode('utf-8')
                analysis_result = analyze_dna(sequence)
                new_sequence = DNASequence(sequence=sequence, analysis_result=analysis_result)
                db.session.add(new_sequence)
                db.session.commit()
                return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return jsonify({"status": "shutting down..."}), 200

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
