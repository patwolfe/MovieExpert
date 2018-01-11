// For local testing(so you don't have to set up the server), comment out the ajax get function and use this local data:
// var rawData =[{"name":"Mean Girls","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_SX300.jpg","score":66},{"name":"Ghost","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTU0NzQzODUzNl5BMl5BanBnXkFtZTgwMjc5NTYxMTE@._V1_SX300.jpg","score":52},{"name":"House on Haunted Hill","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNzUzZDg1OGYtOWE3Mi00OGQ4LWE1NGYtY2FiMTFhZmY2YTg2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg","score":28},{"name":"No Reservations","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1NzQ5MzU1OV5BMl5BanBnXkFtZTcwNzExODU0MQ@@._V1_SX300.jpg","score":50},{"name":"Flyboys","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg5NTkxMF5BMl5BanBnXkFtZTcwNjA4MDUzMQ@@._V1_SX300.jpg","score":47},{"name":"Ronin","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BOWVkYzliZGEtODIxMi00MDQwLThjMDAtNzI3M2NjYjg4NDE5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg","score":67},{"name":"The Pelican Brief","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BODE1NDk3Y2YtNTQzYS00ZTA1LTk3ZDAtZjUxNTc2ZDhlOGRlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg","score":50},{"name":"War of the Worlds","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNDUyODAzNDI1Nl5BMl5BanBnXkFtZTcwMDA2NDAzMw@@._V1_SX300.jpg","score":73},{"name":"Identity","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NzgyNDYzNl5BMl5BanBnXkFtZTYwODM2Nzc2._V1_SX300.jpg","score":64},{"name":"Evil Dead","poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNTQ3OTkwNTgyN15BMl5BanBnXkFtZTcwNTAzOTAzOQ@@._V1_SX300.jpg","score":57}]
// ^^^uncomment this line and comment the get function call and its closing braces/parantheses.

$(document).ready(function(){
    $.get("http://localhost:5000/getRandomMovie",function(rawData, status) {
    	console.log(rawData);    	
    	data = JSON.parse(rawData);
    	console.log(data);
    	i = 0;
    	$("#submitButton").click(function(){
    		if(i >= 10) {
    			console.log(i);
    			$("#heading").text("done");
    		}
    		else {
    			console.log("here");
    			$("#poster").attr("src", data[i].poster);
    			$("#movieName").text(data[i].name);
    			$("#movieScore").text(data[i].score);
    			i++;
    		}
    	});
    });
});