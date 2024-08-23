from app import db

class DNASequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Text, nullable=False)
    analysis_result = db.Column(db.Text)

    def __repr__(self):
        return f"<DNASequence {self.sequence}>"
