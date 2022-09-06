from services.database import db
from models.language import Language


class Film(db.Model):
    """
    Film Table
    """
    film_id = db.Column(db.String(50),primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(500))
    release_year = db.Column(db.String(4))
    language_id = db.Column(db.Integer, db.ForeignKey('language.language_id'),
        nullable=False)
    rental_duration = db.Column(db.Integer)
    rental_rate = db.Column(db.Float)
    length = db.Column(db.Integer)
    replacement_cost = db.Column(db.Float)
    rating = db.Column(db.String(10))
    special_features = db.Column(db.String(500))


film_actor = db.Table('film_actor',
    db.Column('film_id',db.ForeignKey('film.film_id')),
    db.Column('actor_id',db.ForeignKey('actor.actor_id'))
)



