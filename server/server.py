from flask import Flask
from flask import jsonify
import tmdbsimple as tmdb
from requests.exceptions import HTTPError
import random

tmdb.API_KEY = '1c12a973351094b6ef09c2ab1f186f6e'

app = Flask(__name__)

@app.route('/getRandomMovie', methods=['GET'])
def send_movie():
	movie = None
	votes = 0
	response = None
	while movie is None or votes < 250:
		print("Looping")
		try:
			id = random.randrange(1, 450000)
			movie = tmdb.Movies(id)
			repsonse = movie.info()
		except HTTPError:
			print("httperror")
			movie = None
		else:
			votes = movie.vote_count
			print(votes)
	return movie.title

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)