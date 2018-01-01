var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
const imdb = require('imdb-api');
const tmdb = require('tmdbv3').init('1c12a973351094b6ef09c2ab1f186f6e')
var Promise = require('bluebird');

var promiseWhile = function(condition, action) {
    var resolver = Promise.defer();

    var loop = function() {
        if (!condition()) return resolver.resolve();
        return Promise.cast(action())
            .then(loop)
            .catch(resolver.reject);
    };

    process.nextTick(loop);

    return resolver.promise;
};

app.get('/randomMovie', async function(request, response) {
	var found = false;
	promiseWhile(function() {return found === false}, function() {
		console.log("calling api");
		return new Promise(function(resolve, reject) {
			var range = 45000;
			var start = 1;
			var idNum = Math.floor((Math.random() * range) + start);
			var movie = null;
			console.log("inside promise");
			tmdb.movie.info(idNum, function(error, res) {
				console.log("getting movie");
				movie = res; 
				if (movie != null && movie.vote_count >100) {
					console.log("Found a movie");
					console.log(movie);
					found = true;
				}
				resolve();
			})
		})
	})
	.then(()=>console.log(movie));

})

function getRating(movieInfo){
	var ratings = movieInfo.ratings;
	var numRatings = ratings.length;
	var tomatoMeter = "-1%";
	for (i = 0; i < numRatings; i++) {
		if(ratings[i].Source === "Rotten Tomatoes") {
			tomatoMeter = ratings[i].Value;
			console.log(tomatoMeter);
		}
	}
	var rating = tomatoMeter.slice(0, -1);
	console.log(rating);
	return rating;
}

function parseMovie(movie) {
	var title = movie.title;
	var poster = movie.poster;
	var rating = getRating(movie);
	var infoJson = {"title": title, "poster": poster, "tomatoMeter": rating};
	return infoJson;
}

function getRandomMovie(callback) {

	/*imdb.getById(idString, {apiKey: 'd547fa41', timeout: 30000
	}).catch(error=>{console.log("error"); movie = null;});*/
	return movie;
}

function getValidMovie(callback) {
	var found = false;
	getRandomMovie(function(error, movie) {
		console.log(movie);
		if(movie !== null) {
			found = true; 
			console.log("Found")
		} else {
			console.log("Not found")
		}
	console.log("returing");
	return movie;
	});
	callback();

}
app.listen(process.env.PORT || 8080);	