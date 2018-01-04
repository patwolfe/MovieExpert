from flask import Flask
from flask import jsonify
import mysql.connector
from requests.exceptions import HTTPError
import random
import omdb
omdb.set_default('apikey', 'd547fa41')
omdb.set_default('tomatoes', True)

app = Flask(__name__)

@app.route('/getRandomMovie', methods=['GET'])
def send_movie():

	movieName = "";

	while(movieName == ""):
		id = random.randrange(2, 2569)
		cnx = mysql.connector.connect(user='root', password='Memory67',
	                              host='127.0.0.1',
	                              database='movieData')
		cursor = cnx.cursor(dictionary=True)

		query = ("SELECT * FROM movies WHERE table_id=%s")


		cursor.execute(query, (id,))
		for row in cursor:
			movieName = row["title"]
	cursor.close()
	cnx.close()

	response = omdb.get(title=movieName)
	score = response["metascore"]
	poster = response["poster"]
	jsonresposne = '{"name":"' + movieName + '","poster":"' + poster + '","score":' + score +'}'  
	return jsonresposne
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)