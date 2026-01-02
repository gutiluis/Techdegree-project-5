# model class for adding and editting project information:
# title, description, date, skills practiced, github repo
# connect to the database
# the database should contain at least the 4 previous projects
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Text, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    description: Mapped[str] = mapped_column(Text)
    skills: Mapped[str] = mapped_column(Text)
    github_repo: Mapped[str] = mapped_column(Text, unique=True)




    def __repr__(self):
        return f'''<Project (Title: {self.title}
                Description: {self.description}
                Skills: {self.skills}
                Github: {self.github_repo})'''

