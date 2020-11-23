from datetime import datetime
import pytz
from gameinfo import db, login_manager


class Game(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    platform = db.Column(db.Text, unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    publisher = db.Column(db.Text, nullable=False)
    na_sales = db.Column(db.Float, nullable=False)
    eu_sales = db.Column(db.Float, nullable=False)
    jp_sales = db.Column(db.Float, nullable=False)
    other_sales = db.Column(db.Float, nullable=False)
    global_sales = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"User('{self.rank}', '{self.name}', '{self.platform}', '{self.year}', '{self.genre}', '{self.publisher}')"