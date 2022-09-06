from email.policy import default
from re import search
from turtle import title
from urllib import request
from flask import Flask,render_template,request
from services.database import db
from models.actor import Actor
from models.film import Film
import sqlite3



app = Flask(__name__,static_url_path='/static')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/sakila_master.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    
    return render_template("index.html",title="Sakila Home")

@app.route("/actors")
def actors():
    ROWS_PER_PAGE = 10
    page = request.args.get('page', 1, type=int)
    actors = Actor.query.paginate(page,per_page=ROWS_PER_PAGE)
    return render_template("actors.html",title="Sakila - Manage Actors",rows = actors)

@app.route("/films")
def films():
    ROWS_PER_PAGE = 10
    
    actor = request.args.get('actor')
    page = request.args.get('page',1,type=int)
    if actor is None:
        
        films = Film.query.paginate(page,per_page=ROWS_PER_PAGE)
        return render_template("films.html",title="Sakila - Films", rows=films)
    else:
        actor = Actor.query.filter_by(actor_id=actor).first()
        return render_template('film_actors.html',title="Sakila - Films Results",rows=actor.films)
        
if __name__=="__main__":
    app.run(debug = True, host='0.0.0.0', port=5000)
