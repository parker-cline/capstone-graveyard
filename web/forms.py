from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length


class IdeaSubmitForm(FlaskForm):
    title = StringField("Idea Name", validators=[DataRequired(), Length(max=100)])

    description = TextAreaField(
        "Idea Description", validators=[DataRequired(), Length(max=1000)]
    )

    # five tags to choose from: computer science, business, arts and humanities, natural sciences, and social sciences
    tags = SelectMultipleField('What majors would be interested in this project?',
        choices=[
            ("cs", "Computational Sciences"),
            ("b", "Business"),
            ("ah", "Arts and Humanities"),
            ("ns", "Natural Sciences"),
            ("ss", "Social Sciences")
        ]
    )

