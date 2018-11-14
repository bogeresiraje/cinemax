from cinemax.app import db
from cinemax.app_dir.helper import *

import datetime


movie_showtime = db.Table('movie_showtime',
	db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
	db.Column('showtime_id', db.Integer, db.ForeignKey('show_time.id'))
	)


class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	created_date = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
	show_date = db.Column(db.DateTime)
	link = db.Column(db.String(100), unique=True)
	show_period = db.relationship('ShowTime', secondary=movie_showtime, backref=db.backref('movies', lazy='dynamic'))

	def __init__(self, *args, **kwargs):
		super(Movie, self).__init__(*args, **kwargs)
		self.set_link()

	def __repr__(self):
		return '<Movie: %s>' % self.title

	def set_link(self):
		self.link = self.title


class ShowTime(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	start_time = db.Column(db.Integer)
	end_time = db.Column(db.Integer)
	data = db.Column(db.Unicode(4000))
	total_sales = db.Column(db.Integer)
	link = db.Column(db.String(100))
	seats_remained = db.Column(db.Integer)

	def __init__(self, *args, **kwargs):
		super(ShowTime, self).__init__(*args, **kwargs)
		self.data = [['*' for x in range(20)] for y in range(16)]
		self.total_sales = 0
		self.seats_remained = 320

	def __repr__(self):
		return '<ShowTime: %s>' % self.start_time

	def set_link(self):
		if self.movies.all():
			movie = self.movies.all()[0]
			self.link =  movie.title.replace(' ', '_') + '_' + str(self.start_time)


	def reset(self):
		self.__init__()

	def book(self, seats, twin=False):
		new_data = to_array(self.data)

		if twin:
			for pos in seats:
				for seat in pos:
					if new_data[seat[0]][seat[1]] == '*':
						new_data[seat[0]][seat[1]] = '#'
						self.total_sales += self.price(pos)
						self.seats_remained -= 1
					elif new_data[seat[0]][seat[1]] == '#':
						print("already booked")
					else:
						new_data[seat[0]][seat[1]] == 'foo'
		else:
			for seat in seats:
				if new_data[seat[0]][seat[1]] == '*':
					new_data[seat[0]][seat[1]] = '#'
					self.total_sales += self.price(seat)
					self.seats_remained -= 1
				elif new_data[seat[0]][seat[1]] == '#':
					print("already booked")
				else:
					new_data[seat[0]][seat[1]] == 'foo'

		self.data = new_data


	def reserve(self, seats, twin=False):
		new_data = to_array(self.data)
		if twin:
			for pos in seats:
				for seat in pos:
					if new_data[seat[0]][seat[1]] == '*':
						new_data[seat[0]][seat[1]] = 'o'
						self.seats_remained -= 1

					elif new_data[seat[0]][seat[1]] == 'o':
						print("already reserved")
					else:
						new_data[seat[0]][seat[1]] == 'foo'
		else:
			for seat in seats:
				if new_data[seat[0]][seat[1]] == '*':
					new_data[seat[0]][seat[1]] = 'o'
					self.seats_remained -= 1

				elif new_data[seat[0]][seat[1]] == '#':
					print("already reserved")
				else:
					new_data[seat[0]][seat[1]] == 'foo'
		self.data = new_data

	def price(self, seat):
		twin, economy, vvip, vip = seat_prices()
		'''
		twins_seats, vvip_seats, vip_seats, economy_seats = [], [], [], []
		for x in range(1, 17):
			for y in range(1, 21):
				if x == 1 or x == 2:
					if y >= 5 and y <= 15:
						twins_seats.append((x, y))
					vvip_seats.append((x, y))
				elif x >= 3 and x <= 8:
					vip_seats.append((x, y))
				else:
					economy_seats.append((x, y))
		'''
		tw_seats = get_twin()
		vv_seats = get_vvip()
		vi_seats = get_vip()
		ec_seats = get_economy()

		if seat in tw_seats:
			return twin
		elif seat in vv_seats:
			return vvip
		elif seat in vi_seats:
			return vip
		elif seat in ec_seats:
			return economy
		else:
			return -1

	def available_twin(self):
		new_data = to_array(self.data)
		positions = get_twin()
		# available = [seat for seat in positions if new_data[seat[0]][seat[1]] == '*']
		seats = [pos for pos in positions if new_data[pos[0][0]][pos[0][1]] == '*']
		print(seats)
		seat_keys = twin_seats()
		keys = seat_keys.keys()
		return [key for key in keys  if seat_keys[key] in seats]

	def available_vvip(self):
		new_data = to_array(self.data)
		positions = get_vvip()
		available = [seat for seat in positions if new_data[seat[0]][seat[1]] == '*']
		seat_keys = vvip_seats()
		keys = seat_keys.keys()
		return [key for key in keys  if seat_keys[key] in available]

	def available_vip(self):
		new_data = to_array(self.data)
		positions = get_vip()
		available = [seat for seat in positions if new_data[seat[0]][seat[1]] == '*']
		seat_keys = vip_seats()
		keys = seat_keys.keys()
		return [key for key in keys  if seat_keys[key] in available]

	def available_economy(self):
		new_data = to_array(self.data)
		positions = get_economy()
		available = [seat for seat in positions if new_data[seat[0]][seat[1]] == '*']
		seat_keys = economy_seats()
		keys = seat_keys.keys()
		return [key for key in keys  if seat_keys[key] in available]
