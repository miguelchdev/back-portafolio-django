"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Bio, Skill, Project , Contact
api = Blueprint('api', __name__)

@api.route('/bio/')
def bios():
    bios = Bio.query.all()
    response = { 'bios': [bio.to_dict() for bio in bios] }
    return jsonify(response)

@api.route('/bio/<int:id>/')
def bio(id):
    bio = Bio.query.get(id)
    response = bio.to_dict()
    return jsonify(response)

@api.route('/project/')
def projects():
    projects = Project.query.all()
    response = { 'projects': [project.to_dict() for project in projects] }
    return jsonify(response)

@api.route('/project/<int:id>/')
def project(id):
    project = Project.query.get(id)
    response = project.to_dict()
    return jsonify(response)

@api.route('/contacts/')
def contacts():
    projects = Contact.query.all()
    response = { 'contacts': [project.to_dict() for project in projects] }
    return jsonify(response)
