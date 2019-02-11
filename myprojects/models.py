"""
models.py
- Data clases for portafolio app
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bio(db.Model):
    __tablename__ = 'bios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    role = db.Column(db.Text)
    about = db.Column(db.Text)
    skills = db.relationship('Skill', backref="bio", lazy=False)
    contacts = db.relationship('Contact', backref="bio", lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name, role=self.role, about=self.about, skills=[skill.to_dict() for skill in self.skills], contacts={contact.name: contact.link for contact in self.contacts})


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    link = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title, link=self.link, description=self.description, img=self.image)


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    bio_id = db.Column(db.Integer, db.ForeignKey('bios.id'))

    def to_dict(self):
        return self.name


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    link = db.Column(db.Text)
    bio_id = db.Column(db.Integer, db.ForeignKey('bios.id'))

    def to_dict(self):
        return dict(name=self.name, link=self.link)
