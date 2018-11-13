from flask import render_template, redirect, url_for, request
from cinemax.app import app
from cinemax.models import *


@app.route('/')
def home():
	movies = list()
	upcoming = list()
	movies = Movie.query.all()
	if movies:
		upcoming = movies[0]
	return render_template('home.html', movies=movies, upcoming=upcoming)

@app.route('/booking/<movie_link>')
def book(movie_link):
	show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
	total_sales = show_time.total_sales;
	seats_remained = show_time.seats_remained;
	return render_template('/booking/booking.html', movie_link=movie_link,
		total_sales=total_sales, seats_remained=seats_remained)

@app.route('/booking/<movie_link>/<int:category>/<int:status>', methods=['GET', 'POST'])
def book_seats(movie_link, category, status):
	show_time = ShowTime.query.filter(ShowTime.link == movie_link).first()
	keys = [key for key in request.form];

	# twin seats and book
	if category == 1 and status == 1:
		positions = get_positions(keys,twin=True)
		show_time.book(positions)

	# twin seats and reserved
	if category == 1 and status == 2:
		positions = get_positions(keys,twin=True)
		show_time.reserve(positions)

	#vvip and book
	if category == 2 and status == 1:
		positions = get_positions(keys,vvip=True)
		show_time.book(positions)

	# vvip and reserve
	if category == 2 and status == 2:
		positions = get_positions(keys,vvip=True)
		show_time.reserve(positions)

	# vip seats and book
	if category == 3 and status == 1:
		positions = get_positions(keys,vip=True)
		show_time.book(positions)

	# vip seats and reserve
	if category == 3 and status == 2:
		positions = get_positions(keys,vip=True)
		show_time.reserve(positions)

	#economy and book
	if category == 4 and status == 1:
		positions = get_positions(keys, economy=True)
		show_time.book(positions)

	# economy and reserve
	if category == 4 and status == 2:
		positions = get_positions(keys, economy=True)
		show_time.reserve(positions)

	else:
		pass

	db.session.commit()
	return redirect(url_for('book', movie_link=movie_link))
