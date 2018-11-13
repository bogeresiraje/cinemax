from cinemax import app, models
from cinemax.front import views
from cinemax.app import app, db
from cinemax.app_dir.blueprint import booking

app.register_blueprint(booking, url_prefix='/appdir/booking')

if __name__ == '__main__':
    app.run(debug=True)
