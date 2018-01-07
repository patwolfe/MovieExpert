from flask import Flask
from flask import jsonify
from flask import request
import mysql.connector
from requests.exceptions import HTTPError
import random
import omdb
omdb.set_default('apikey', 'd547fa41')
omdb.set_default('tomatoes', True)

app = Flask(__name__)

@app.route('/getRandomMovie', methods=['GET'])
def get_movie():

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



@app.route('/getLeaderboard', methods=['GET'])
def get_leaders():
	leaders = '{"leaders": [' 
	cnx = mysql.connector.connect(user='root', password='Memory67',
							  host='127.0.0.1',
							  database='movieData')
	cursor = cnx.cursor(dictionary=True)

	query = ("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 10")
	cursor.execute(query)
	for row in cursor:
		score = str(row["Score"])
		person = '{"name": "' + row["Name"] + '", "score":' + score + '}'
		leaders += person
		leaders += ','
	leaders = leaders[:-1]
	cursor.close()
	cnx.close()
	leaders += ']}'
	return leaders

@app.route('/sendScore', methods=['POST'])
def send_score():
	name = request.form.get('name')
	score = request.form.get('score')
	cnx = mysql.connector.connect(user='root', password='Memory67',
							  host='127.0.0.1',
							  database='movieData')
	cursor = cnx.cursor(dictionary=True)
	
	user_data = (name, score)
	add_user = ("INSERT INTO leaderboard (Name, Score) VALUES (%s, %s)")
	cursor.execute(add_user, user_data)
	cnx.commit()
	cursor.close()
	cnx.close()
	test = "Good"
	return test


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)