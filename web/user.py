from flask import Blueprint, render_template
import os

user = Blueprint('user', __name__)

@user.route('/about_me')
def about_me():
    return render_template('about_me.html')

@user.route('/projects')
def projects():
    return render_template('projects.html',content=os.listdir("static/projects"))

@user.route('/designs')
def designs():
    return render_template('designs.html',content=os.listdir("static/designs"))

@user.route('/illustrations')
def illustrations():
    return render_template('illustrations.html',content=os.listdir("static/illustrations"))


