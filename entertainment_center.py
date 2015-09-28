import media
import fresh_tomatoes

#Create six instances of latest good movies
mad_max = media.Movie("Mad Max: Fury Road",
                      "An apocalyptic story set in the furthest reaches of our planet",
                      "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
                      "https://www.youtube.com/watch?v=b_4nzm9ICuo")

jurrasic_world = media.Movie("Jurassic World ",
                      "Twenty-two years after the events of Jurassic Park, Isla Nublar now features a fully functioning dinosaur theme park, Jurassic World",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                      "https://www.youtube.com/watch?v=ZXiahojLbOw")

tomorrowland = media.Movie("Tomorrowland",
                      "Bound by a shared destiny, a bright, optimistic teen bursting with scientific curiosity and a former boy-genius inventor jaded by disillusionment embark on a danger-filled mission to unearth the secrets of an enigmatic place somewhere in time and space that exists in their collective memory as Tomorrowland.",
                      "https://upload.wikimedia.org/wikipedia/en/8/80/Tomorrowland_poster.jpg",
                      "https://www.youtube.com/watch?v=lWZ7O-RrATY")

san_andreas = media.Movie("San Andreas",
                      "In the aftermath of a massive earthquake in California, a rescue-chopper pilot makes a dangerous journey across the state in order to rescue his estranged daughter.",
                      "https://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg",
                      "https://www.youtube.com/watch?v=yftHosO0eUo")

avenger = media.Movie("Avengers: Age of Ultron",
                      "When Tony Stark tries to jumpstart a dormant peacekeeping program, things go awry",
                      "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                      "https://www.youtube.com/watch?v=tmeOjFno6Do")

boy_hood = media.Movie("Boy Hood",
                       "A story about a boy growing up from six years old to eighteen in Texas",
                       "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                       "https://www.youtube.com/watch?v=Y0oX0xiwOv8")

#Add six instances of class Movie to a list
movies = [mad_max, jurrasic_world, tomorrowland, san_andreas, avenger, boy_hood]

#Create a fresh_tomatoes.html document on disc and show it in the web browser
fresh_tomatoes.open_movies_page(movies)

