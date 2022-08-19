from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm


class CreatePostForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    subtitle = StringField("Подзаголовок", validators=[DataRequired()])
    img_url = StringField("Изображение (URL)", validators=[DataRequired(), URL()])
    body = CKEditorField("Содержание", validators=[DataRequired()])
    submit = SubmitField("Разместить")


class RegisterForm(FlaskForm):
    email = StringField("Эл. адрес", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    email = StringField("Эл. адрес", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")


class CommentForm(FlaskForm):
    comment = CKEditorField('Комментарий', validators=[DataRequired()])
    submit = SubmitField("Разместить")


class ContactForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Эл. адрес", validators=[DataRequired(), Email()])
    phone_number = StringField("Телефонный номер", validators=[DataRequired()])
    message = StringField("Сообщение", validators=[DataRequired()])
    submit = SubmitField("Отправить")
