from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from .form import RegistrationForm,CreateFilm,Vibor,ByForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,LoginManager,login_user,logout_user,login_required,current_user
app = Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db= SQLAlchemy(app)
migrate=Migrate(app,db)
login = LoginManager(app)
login.login_view='loginFOrm'


class Admin(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.Integer, nullable=False)


    def hash_password(self,password):
        self.password= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)




class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    image_film=db.Column(db.String, nullable=False)
    film_name=db.Column(db.String, nullable=False,unique=True)#назва
    protagonists=db.Column(db.String, nullable=False) #головні герої
    genre=db.Column(db.String, nullable=False) #жанр
    graduation_year=db.Column(db.Integer, nullable=False) #рік випуску
    rating=db.Column(db.Integer, nullable=False)# рейтинг
    country=db.Column(db.String, nullable=False)# країна
    time=db.Column(db.Integer, nullable=False)# время фільму



@login.user_loader
def user_loader(id):
    return Admin.query.get(id)




@app.route('/',methods=['GET','POST'])
def main():
    image = Film.query.all()
    form = Vibor()
    if form.validate_on_submit():
        genre = form.genre.data
        graduation_year=form.graduation_year.data
        rating=form.rating.data
        image=Film.query.filter_by(genre=genre,graduation_year=graduation_year,rating=rating)
        return render_template('home.html',image=image,form=form)
    return render_template('home.html',image=image,form=form)



@app.route('/Admin',methods=['GET','POST'])
def admin():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        check=form.remember_me.data
        username1=Admin.query.filter_by(name=username).first()
        if username1 is None or not username1.check_password(password):
            return redirect ('/Admin')
        login_user (username1,remember=check)
        return redirect('/create_film')
    return render_template('loginadmin.html',form=form)

@app.route('/Film<int:id>',methods=['GET','POST'])
def film(id):
    film=Film.query.get(id)
    return render_template('film.html',film=film)


@app.route('/create_film',methods=['GET','POST'])
@login_required
def createfilm():
    form = CreateFilm()
    if form.validate_on_submit():
        text=form.text.data
        image_film = form.image_film.data
        image_film.save(f"app/static/photo/{image_film.filename}")
        film_name = form.film_name.data
        protagonists = form.protagonists.data
        genre = form.genre.data
        graduation_year = form.graduation_year.data
        rating = form.rating.data
        country = form.country.data
        time = form.time.data
        CreateFilms=Film(text=text,image_film=f"/static/photo/{image_film.filename}"
                         ,film_name=film_name,protagonists=protagonists,genre=genre,
                         graduation_year=graduation_year,rating=rating,country=country,
                         time=time
                         )
        try:
            db.session.add(CreateFilms)
            db.session.commit()
        except IntegrityError:
            return render_template('create_film.html', form=form,text="помилка")
    return render_template('create_film.html', form=form)

@app.route('/by')
def by():
    return render_template('by.html')

@app.route('/by1',methods=['GET','POST'])
def by1():
    form = ByForm()
    return render_template('by1.html',form=form)

@app.route('/by2',methods=['GET','POST'])
def by2():
    form = ByForm()
    return render_template('by2.html',form=form)

#название сата MovieVibe большая буква м логотип чорно красній цвет