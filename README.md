# MovieScoreGuessing

# Demo

https://movieexpert.herokuapp.com/

## Development Notes

### Server:
I think express(JS) or flask(Python) should be sufficient for the server.

- GET randMovie API
We can have this return a movie name, image, and score
in JSON form. Hopefully the IMDB api includes images, everything else should be
easy.
Make sure it's a movie people have actually heard of by using a # ratings
threshold before returning
We can probably have this just return n random movies to save time.

- POST addScore API
Add the score to the api if its in the top 10 scores and return its position
If it's less than the 10th best return -1.

- GET getLeaders API
Returns top 10 players and their scores. We could have it return the number of
people on the leaderboard to check if 10 people have played or we can just
be hacky and insert 10 players into the leaderboard at the start to avoid
that issue.

### Front End:
HTML, CSS, JavaScript (jQuery should be fine)

3 pages (start and one for game one for leaderboard)


Start
- Start page just takes a username via text box. Idk how to pass this to
the next page but shouldn't be too hard. We can put it in session storage
or send it through the GET request in a query string. Since there's no password
or anything it shouldn't be a big deal.


Main
- Main page will display all the info and have an input box for the user's guess
Upon submitting their guess, the page will show the real score and how many
points they got.
- We'll do this for n movies (n can be whatever we decide is a good number)
Then tell them if they made it onto the leaderboard
- score formula for a single guess: 100 - (Real - Guess)
We can probably make this fancier but for now this should work.
- 2 States: Guessing and Result
Switch from guessing to result when you submit a guess, from result
to guessing when they hit the next button (need to figure out how to have
  this button appear and disappear/become inactive hopefully that's easy in
  jQuery)


Leaderboard
- After the nth guess we can take the user to the leaderboard page. This will
show their score and tell them if they made it to the leaderboard or not. Also
will have a play again button
