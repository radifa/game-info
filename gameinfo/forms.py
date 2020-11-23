from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange


class RegistrationForm(FlaskForm):
    username = StringField('Nama',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    nim = IntegerField('NIM',
                        validators=[DataRequired(), NumberRange(min=18100000, 
                        max=18199999, message='Hanya untuk anggota IMT "Signum" ITB')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Konfirmasi Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Nama ini telah terdaftar, Silahkan gunakan nama lain.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email ini telah terdaftar, Silahkan gunakan email lain.')

    def validate_nim(self, nim):
        user = User.query.filter_by(nim=nim.data).first()
        if user:
            raise ValidationError('NIM ini telah terdaftar.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Ingat saya')
    submit = SubmitField('Masuk')


class UpdateAccountForm(FlaskForm):
    username = StringField('Nama',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Foto Profil', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Nama tersebut sudah digunakan.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email tersebut sudah digunakan.')

class RenterForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Pinjam')

class BookForm(FlaskForm):
    title = StringField('Judul Buku',
                        validators=[DataRequired()])
    category = StringField('Kategori',
                        validators=[DataRequired()])
    submit = SubmitField('Tambah')    

class ReturnForm(FlaskForm):
    agree = BooleanField('Buku sudah saya kembalikan',
                        validators=[DataRequired()])
    submit = SubmitField('Kembalikan')

class SearchForm(FlaskForm):
    kata = StringField('Game Title', validators=[DataRequired()])
