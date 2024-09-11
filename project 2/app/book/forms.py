from flask_wtf import FlaskForm
from wtforms import StringField, FileField, IntegerField
from wtforms.validators import DataRequired

class BooksForm(FlaskForm):
    Booktitle = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    pages = IntegerField('Pages', validators=[DataRequired()])
    image = FileField('Cover Photo')