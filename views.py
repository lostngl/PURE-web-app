from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, 'views')

@views.route("/")
def home():
    return render_template('structure.html', name = 'appa', power = 'melon')

@views.route("/profile")
def profile():
    return render_template("profile.html")

#this whole section is supposed to change depending on username given, but i cant fix it so
# @views.route("/username")
# def username():
#     args = request.args
#     name = args.get('name')
#     return render_template("structure.html", name = name)

@views.route('/json')
def get_json():
    return jsonify({'name': 'appa', 'power': 10, 'melon': 'stolen'})
