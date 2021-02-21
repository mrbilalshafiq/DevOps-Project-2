from flask_wtf import FlaskForm
from wtforms import SubmitField

class IndexForm(FlaskForm):
    submit = SubmitField('Get Prize!')
