from flask import Blueprint, render_template, jsonify, request, abort
from cinemax.app_dir.helper import *
from cinemax.models import ShowTime

booking = Blueprint('booking', __name__)

@booking.route('/<movie_link>')
@booking.route('/')
def book_home(movie_link=None):
	if movie_link:
		show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
		chart = show_time.data
		chart = to_array(chart)
		return jsonify({"chart": chart, "movie_link": movie_link})
	else:
		movie_link = request.args.get('movie_link')
		show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
		chart = show_time.data
		chart = to_array(chart)
		return jsonify({"chart": chart, "movie_link": movie_link})

@booking.route('/<movie_link>/<int:category>')
def check_seats(movie_link, category):
	available = None
	show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
	if(category == 1):
		# twin seats
		available = show_time.available_twin()
	elif(category == 2):
		# very vvip
		available = show_time.available_vvip()
	elif(category == 3):
		# vip
		available = show_time.available_vip()
	elif(category == 4):
		# economy
		available = show_time.available_economy()
	else:
		pass

	if available:
		return jsonify({'available': available})


@booking.route('/movie')
def check():
	available = None
	movie_link = request.args.get('movie_link')
	category = request.args.get('category')
	category = int(category)
	show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
	if(category == 1):
		# twin seats
		available = show_time.available_twin()
	elif(category == 2):
		# very vvip
		available = show_time.available_vvip()
	elif(category == 3):
		# vip
		available = show_time.available_vip()
	elif(category == 4):
		# economy
		available = show_time.available_economy()
	else:
		pass

	return jsonify({'available': available})
