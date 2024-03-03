from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField,SelectField,IntegerField,FileField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileRequired

class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    remember_me=BooleanField('remember_me')
    submit=SubmitField()



class CreateFilm(FlaskForm):
    text =StringField('Текст',validators=[DataRequired()])
    image_film =FileField('Картинка_фільму',validators=[FileRequired()])
    film_name =StringField('Назва_фільму',validators=[DataRequired()])   # назва
    protagonists =StringField('Головні_герої',validators=[DataRequired()])   # головні герої
    genre =SelectField('Жанр',validators=[DataRequired()],choices=[('Бойовик', 'Бойовик'), ('Детектив', 'Детектив'), ('Драма', 'Драма'), ('Комедія', 'Комедія'), ('Пригодницький', 'Пригодницький'), ('Трагедія', 'Трагедія'), ('Історичний', 'Історичний')])   # жанр
    graduation_year =SelectField('Рік_випуску',validators=[DataRequired()],choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'),('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')])   # рік випуску
    rating =SelectField('Рейтинг',validators=[DataRequired()],choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])   # рейтинг
    country =StringField('Країна',validators=[DataRequired()]) # країна
    time =StringField('Час_фільму',validators=[DataRequired()])   # время фільму
    submit=SubmitField()

class Vibor(FlaskForm):
    graduation_year = SelectField('Рік_випуску', validators=[DataRequired()],
                                  choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
                                           ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'),
                                           ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'),
                                           ('2022', '2022'), ('2023', '2023')])  # рік випуску
    rating = SelectField('Рейтинг', validators=[DataRequired()],
                         choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])  # рейтинг
    genre = SelectField('Жанр', validators=[DataRequired()],
                        choices=[('Бойовик', 'Бойовик'), ('Детектив', 'Детектив'), ('Драма', 'Драма'),
                                 ('Комедія', 'Комедія'), ('Пригодницький', 'Пригодницький'), ('Трагедія', 'Трагедія'),
                                 ('Історичний', 'Історичний')])  # жанр
    submit=SubmitField()

class ByForm(FlaskForm):
    username= StringField('Імя та прізвище',validators=[DataRequired()])
    bankcard=StringField('Номер карти',validators=[DataRequired()])
    submit=SubmitField()