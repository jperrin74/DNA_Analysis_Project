from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class DNAForm(FlaskForm):
    sequence = TextAreaField('DNA Sequence', validators=[DataRequired()])
    file = FileField('Upload DNA File', validators=[FileAllowed(['txt'], 'Text files only!')])
    submit = SubmitField('Analyze')
