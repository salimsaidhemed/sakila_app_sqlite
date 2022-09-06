from services.database import db
from models.film import film_actor

class Actor (db.Model):
    """
    Actor Table
    """
    actor_id = db.Column(db.String(50),primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    films = db.relationship('Film',secondary=film_actor,backref='actors')
    
    def __repr__(self) -> str:
        return '<{} {}>'.format(self.first_name,self.last_name)

