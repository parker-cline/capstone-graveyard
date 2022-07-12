from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    TextAreaField
)
from wtforms.validators import DataRequired, Length


class IdeaSubmitForm(FlaskForm):
    title = StringField(
        "Idea Name", validators=[DataRequired(), Length(max=100)]
    )
    
    description = TextAreaField(
        "Idea Description", validators=[DataRequired(), Length(max=1000)]
    )