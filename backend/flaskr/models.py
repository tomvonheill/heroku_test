from sqlalchemy import Integer, Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['HEROKU_POSTGRESQL_YELLOW_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''

class CrudMixin:
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()

class PromotionManager(db.Model, CrudMixin):  
  __tablename__ = 'PromotionManager'

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  phone_number=Column(String)

  def __init__(self, id,first_name,last_name, phone_number=''):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = catchphrase

  def format(self):
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'phone_number': self.catchphrase}
