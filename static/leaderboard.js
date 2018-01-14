$(document).ready(function(){
	$.get("https://damp-depths-96034.herokuapp.com/getLeaderboard", function(rawData, status){
	    response = JSON.parse(rawData);
	    leaders = response.leaders;
	    size = leaders.length;
	    console.log(size);
	    for(i = 0; i < size; i++) {
	    	console.log("inside for loop");
	    	var name = leaders[i].name;
	    	var score = leaders[i].score;
	    	var markup = "<tr><td>" + name + "</td><td>" + score + "</td></tr>";
	    	$("table tbody").append(markup);
		}
	 });
});