import media
import fresh_tomatoes

# Create six instances of latest good movies
mad_max = media.Movie("Mad Max: Fury Road",
                      "George Miller",
                      "7 May 2015",
                      "An apocalyptic story set in the furthest reaches o" +
                      "f our planet",
                      "https://upload.wikimedia.org/wikipedia/en/2/23/Max" +
                      "_Mad_Fury_Road_Newest_Poster.jpg",
                      "https://www.youtube.com/watch?v=b_4nzm9ICuo")

jurrasic_world = media.Movie(
                      "Jurassic World ",
                      "Colin Trevorrow",
                      "May 29, 2015",
                      "Twenty-two years after the events of Jurassic Park," +
                      " Isla Nublar now features a fully functioning dinos" +
                      "aur theme park, Jurassic World",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Jura" +
                      "ssic_World_poster.jpg",
                      "https://www.youtube.com/watch?v=ZXiahojLbOw")

tomorrowland = media.Movie(
                      "Tomorrowland",
                      "Brad Bird",
                      "May 8, 2015",
                      "Bound by a shared destiny, a bright, optimistic tee" +
                      "n bursting with scientific curiosity and a former " +
                      "boy-genius inventor jaded by disillusionment embark" +
                      " on a danger-filled mission to unearth the secrets " +
                      "of an enigmatic place somewhere in time and space t" +
                      "hat exists in their collective memory as Tomorrowla" +
                      "nd.",
                      "https://upload.wikimedia.org/wikipedia/en/8/80/Tomo" +
                      "rrowland_poster.jpg",
                      "https://www.youtube.com/watch?v=lWZ7O-RrATY")

san_andreas = media.Movie(
                      "San Andreas",
                      "Brad Peyton",
                      "May 27, 2015",
                      "In the aftermath of a massive earthquake in Califor" +
                      "nia, a rescue-chopper pilot makes a dangerous journ" +
                      "ey across the state in order to rescue his estrange" +
                      "d daughter.",
                      "https://upload.wikimedia.org/wikipedia/en/3/38/San_" +
                      "Andreas_poster.jpg",
                      "https://www.youtube.com/watch?v=yftHosO0eUo")

avenger = media.Movie("Avengers: Age of Ultron",
                      "Joss Whedon",
                      "April 13, 2015",
                      "When Tony Stark tries to jumpstart a dormant peacek" +
                      "eeping program, things go awry",
                      "https://upload.wikimedia.org/wikipedia/en/1/1b/Aven" +
                      "gers_Age_of_Ultron.jpg",
                      "https://www.youtube.com/watch?v=tmeOjFno6Do")

boy_hood = media.Movie("Boyhood",
                       "Richard Linklater",
                       "January 19, 2014",
                       "A story about a boy growing up from six years old " +
                       "to eighteen in Texas",
                       "https://upload.wikimedia.org/wikipedia/en/b/bb/Boy" +
                       "hood_film.jpg",
                       "https://www.youtube.com/watch?v=Y0oX0xiwOv8")

# Add six instances of class Movie to a list
movies = [mad_max, jurrasic_world, tomorrowland,
          san_andreas, avenger, boy_hood]

# Create a fresh_tomatoes.html document on disc and show it in the web browser
fresh_tomatoes.open_movies_page(movies)
