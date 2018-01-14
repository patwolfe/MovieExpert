from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask_cors  import CORS
import mysql.connector
from requests.exceptions import HTTPError
import random
import omdb
omdb.set_default('apikey', 'd547fa41')
omdb.set_default('tomatoes', True)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def test():
	return render_template('Startpage.html')
@app.route('/getRandomMovie', methods=['GET'])
def get_movie():
	cnx = mysql.connector.connect(user='c8z9jjk15zhwew0t', password='ut66k8wmevtzgmur',
									  host='qbct6vwi8q648mrn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',									 
									  database='itpo6r2v2r37o2w2')
	cursor = cnx.cursor(dictionary=True)
	jsonresponse = '['
	i = 0
	while i < 10:
		movieName = ""
		while(movieName == ""):
			id = random.randrange(2, 2569)


			query = ("SELECT * FROM movies WHERE table_id=%s")


			cursor.execute(query, (id,))
			for row in cursor:
				movieName = row["title"]
		response = omdb.get(title=movieName)
		if "metascore" in response:
			if response["metascore"] != "N/A":
				score = response["metascore"]
				poster = response["poster"]
				movieInfo = '{"name":"' + movieName + '","poster":"' + poster + '","score":' + score +'}'
				i += 1
				jsonresponse += movieInfo;
				if (i < 10):
					jsonresponse += ','
	cursor.close()
	cnx.close()	
	jsonresponse += ']'
	return jsonresponse



@app.route('/getLeaderboard', methods=['GET'])
def get_leaders():
	leaders = '{"leaders": [' 
	cnx = mysql.connector.connect(user='c8z9jjk15zhwew0t', password='ut66k8wmevtzgmur',
									  host='qbct6vwi8q648mrn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
									  database='itpo6r2v2r37o2w2')
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
	cnx = mysql.connector.connect(user='c8z9jjk15zhwew0t', password='ut66k8wmevtzgmur',
									  host='qbct6vwi8q648mrn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
									  database='itpo6r2v2r37o2w2')
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