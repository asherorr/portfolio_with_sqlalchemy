from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    completion_date = db.Column('Completion Date', db.Date)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text())
    github_link = db.Column('Github Link', db.Text())
    

    def __repr__(self):
            return f'''<Project:
                Name: {self.title}
                Completion Date: {self.date}
                Description: {self.description}
                Skills: {self.skills}
                Github Link: {self.github_link}'''