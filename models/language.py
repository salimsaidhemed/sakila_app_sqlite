from services.database import db


class Language(db.Model):
    """
    Language Table
    """
    language_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    films = db.relationship('Film',backref='language')

    def __repr__(self) -> str:
        return self.name


